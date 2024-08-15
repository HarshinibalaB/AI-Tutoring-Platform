class KnowledgeGraph:
    def __init__(self):
        self.graph = {}

    def add_concept(self, concept):
        if concept not in self.graph:
            self.graph[concept] = []

    def add_relationship(self, parent, child):
        if parent in self.graph:
            self.graph[parent].append(child)
        else:
            self.graph[parent] = [child]

    def get_related_concepts(self, concept):
        return self.graph.get(concept, [])
knowledge_graph = KnowledgeGraph()
knowledge_graph.add_concept('Algebra')
knowledge_graph.add_relationship('Algebra', 'Quadratic Equations')
