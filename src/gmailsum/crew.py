from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.gmailsum.gmail_api import fetch_unread_emails  # Import actual email fetcher

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Gmailsum():
	"""Gmailsum crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def  email_reader(self) -> Agent:
		return Agent(
			config=self.agents_config['email_reader'],
			verbose=True
		)

	@agent
	def email_categorizer(self) -> Agent:
		return Agent(
			config=self.agents_config['email_categorizer'],
			verbose=True
		)

	
	@task
	def fetch_emails_task(self) -> Task:
		return Task(
			config=self.tasks_config['fetch_emails_task'],
			callback=fetch_unread_emails,
		)

	@task
	def categorize_emails_task(self) -> Task:
		return Task(
			config=self.tasks_config['categorize_emails_task'],
			expected_output="Emails classified into High, Medium, Low, or Personal priority.",
            dependencies=[self.fetch_emails_task()],
			output_file='report.md',
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Gmailsum crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
