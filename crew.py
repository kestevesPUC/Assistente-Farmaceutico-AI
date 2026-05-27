from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
import yaml

# =========================
# Knowledge source (PDFs)
# =========================
pdf_tool = PDFKnowledgeSource(
    file_paths=[
        "DOC120.pdf",
        "file.pdf",
        "rdc0301_21_08_2019.pdf"
    ]
)

# =========================
# LLM
# =========================
llm = LLM(
    model="gpt-4o-mini",
    temperature=0
)

# =========================
# Crew Definition
# =========================
@CrewBase
class ComplianceCrew:
    agent_config_path = "config/agents.yaml"
    tasks_config_path = "config/tasks.yaml"

    def __init__(self):
        # Carrega YAML corretamente (CORREÇÃO DO SEU ERRO)
        with open(self.agent_config_path, "r", encoding="utf-8") as f:
            self.agent_config = yaml.safe_load(f)

        with open(self.tasks_config_path, "r", encoding="utf-8") as f:
            self.tasks_config = yaml.safe_load(f)

    # =========================
    # Agent
    # =========================
    @agent
    def especialista_compliance(self) -> Agent:
        return Agent(
            config=self.agent_config["especialista_compliance"],
            verbose=True,
            tools=[],
            llm=llm,
        )

    # =========================
    # Task
    # =========================
    @task
    def responder_pergunta_compliance(self) -> Task:
        return Task(
            config=self.tasks_config["responder_pergunta_compliance"],
        )

    # =========================
    # Crew
    # =========================
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.especialista_compliance()],
            tasks=[self.responder_pergunta_compliance()],
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[pdf_tool],
        )