from crewai import Agent
from .tools import *
from .config import AGENTS_CONFIG

def create_agents():
    """Créer tous les agents métier"""
    
    agents = {}
    
    # Agent Gestionnaire d'intention
    agents['intention_manager'] = Agent(
        role=AGENTS_CONFIG['intention_manager']['role'],
        goal=AGENTS_CONFIG['intention_manager']['goal'],
        backstory=AGENTS_CONFIG['intention_manager']['backstory'],
        tools=[semantic_analyzer_tool, intent_classifier_tool],
        verbose=True,
        allow_delegation=True
    )
    
    # Agent Chef de projet fonctionnel
    agents['functional_pm'] = Agent(
        role=AGENTS_CONFIG['functional_pm']['role'],
        goal=AGENTS_CONFIG['functional_pm']['goal'],
        backstory=AGENTS_CONFIG['functional_pm']['backstory'],
        tools=[requirement_analyzer_tool, functional_spec_tool],
        verbose=True,
        allow_delegation=True
    )
    
    # Agent Chef de projet technique  
    agents['technical_pm'] = Agent(
        role=AGENTS_CONFIG['technical_pm']['role'],
        goal=AGENTS_CONFIG['technical_pm']['goal'],
        backstory=AGENTS_CONFIG['technical_pm']['backstory'],
        tools=[architecture_designer_tool, tech_spec_tool],
        verbose=True,
        allow_delegation=True
    )
    
    # Agent Lead développeur
    agents['lead_developer'] = Agent(
        role=AGENTS_CONFIG['lead_developer']['role'],
        goal=AGENTS_CONFIG['lead_developer']['goal'],
        backstory=AGENTS_CONFIG['lead_developer']['backstory'],
        tools=[code_generator_tool, quality_checker_tool],
        verbose=True,
        allow_delegation=True
    )
    
    # Agent Release manager
    agents['release_manager'] = Agent(
        role=AGENTS_CONFIG['release_manager']['role'],
        goal=AGENTS_CONFIG['release_manager']['goal'],
        backstory=AGENTS_CONFIG['release_manager']['backstory'],
        tools=[deployment_tool, quality_gate_tool],
        verbose=True,
        allow_delegation=True
    )
    
    return agents
