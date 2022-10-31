import aws_cdk as core
import aws_cdk.assertions as assertions

from my_pipeline.my_pipeline_stack import MyPipelineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_pipeline/my_pipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MyPipelineStack(app, "my-pipeline")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
