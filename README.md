# AWS Order Notification System
## 🛠️ Setup Instructions

1. **Create DynamoDB Table**
   - Table name: `Orders`
   - Partition key: `orderId` (String)

2. **Create SNS Topic**
   - Name: `OrderTopic`

3. **Create SQS Queues**
   - `OrderQueue` (Main)
   - `OrderDLQ` (Dead-letter queue)
   - Link DLQ to `OrderQueue` (maxReceiveCount: 3)

4. **Subscribe SQS to SNS**
   - SNS → `OrderTopic` → Add SQS subscription (`OrderQueue`)
   - Update SQS access policy to allow SNS publishing

5. **Create Lambda Function**
   - Name: `OrderProcessor`
   - Language: Python 3.12
   - Attach `AmazonSQSFullAccess` and `AmazonDynamoDBFullAccess`
   - Add SQS trigger from `OrderQueue`
   - Code provided in `lambda_function.py`

6. **Publish Test Message to SNS**

## Flow
![aws drawio](https://github.com/user-attachments/assets/2901947e-d585-4473-858c-c48ee2f54c30)
