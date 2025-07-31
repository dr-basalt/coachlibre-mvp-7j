from crewai import Crew, Process
from .agents import create_agents
from .config import WORKFLOW_CONFIG

def create_okr_evaluation_workflow():
    """Creates the main OKR evaluation workflow"""
    
    agents = create_agents()
    
    # Define the workflow tasks
    tasks = [
        {
            'description': 'Analyze user intention and classify requirements',
            'agent': agents['intention_manager'],
            'expected_output': 'Classified intention with priority and context'
        },
        {
            'description': 'Create functional specifications from analyzed requirements',
            'agent': agents['functional_pm'],
            'expected_output': 'Detailed functional specifications document'
        },
        {
            'description': 'Design technical architecture and implementation plan',
            'agent': agents['technical_pm'],
            'expected_output': 'Technical architecture document with implementation roadmap'
        },
        {
            'description': 'Implement solution following technical specifications',
            'agent': agents['lead_developer'],
            'expected_output': 'Working implementation with code and documentation'
        },
        {
            'description': 'Validate and prepare for release',
            'agent': agents['release_manager'],
            'expected_output': 'Release-ready deliverable with quality validation'
        }
    ]
    
    # Create the crew
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
        max_iter=WORKFLOW_CONFIG['okr_evaluation']['max_iterations']
    )
    
    return crew

def execute_workflow(user_intention: str):
    """Execute the complete workflow with user intention"""
    
    workflow = create_okr_evaluation_workflow()
    
    result = workflow.kickoff(inputs={
        'user_intention': user_intention,
        'quality_threshold': WORKFLOW_CONFIG['okr_evaluation']['threshold']
    })
    
    return result
