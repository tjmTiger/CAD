from typing import TypeAlias
# https://austinmorlan.com/posts/entity_component_system/

################
## Components ##
################

class Component():
    def __init__(self):
        # ex. position, rotation etc.
        pass

"""
horisontal
vertical
radius
length

parallel
perpendicular
coincent
tangent
concentric
equal_radius
distance_between
angle_between
"""

##############
## Entities ##
##############
Entity: TypeAlias = int # Entity is just an id number

##############

class EntityManager():
    def __init__(self):
        self._MAX_ENTITIES = 5000
        self._available_entities = list(range(self._MAX_ENTITIES-1, -1, -1)) # stack of items
        self._entities = list()
        self._signatures = dict()
    
    def create_entity(self):
        entity = self._available_entities.pop()
        self._entities.append(entity)
        return entity
    
    def destroy_entity(self, entity: Entity):
        self._entities.remove(entity)
        self._signatures.pop(entity)
        self._available_entities.append(entity)
    
    def set_signature(self, entity: Entity, signature): # a signature tracks what components an entity has
        self._signatures[entity] = signature
    
    def get_signature(self, entity: Entity):
        return self._signatures[entity]

class ComponentArray():
    def __init__(self):
        pass