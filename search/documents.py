from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from questions.models import Question

@registry.register_document
class QuestionDocument(Document):

    answer = fields.NestedField(properties={
        'pk': fields.IntegerField(),
        'answer': fields.TextField()
    })
    

    class Django:
        model = Question  # The model associated with this Document
        fields = [
            'question',
            'question_searchable_string',
            # 'answer',
        ]

    class Index:
    # Name of the Elasticsearch index
        name = 'questions'