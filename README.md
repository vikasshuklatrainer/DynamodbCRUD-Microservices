# Dynamodb CRUD-Micro services(Lambda)

# What we are going to build 

![What we are building](./images/What-we-are-building.png)



## Lets Create a AWS DynamoDB Table

```html
STEP 1 — Create DynamoDB Table

Open DynamoDB → Tables → Create table

Table name: Students

Partition key:

Name: studentId

Type: String

Leave defaults → Create table


```

![Create dynamo db table](./images/Create-dynamo-db-table.png)

## STEP 2 — Create IAM Role for Lambda

![Create Iam 1](./images/create-iam-1.png)

![Create Iam 2](./images/create-iam-2.png)

![Create Iam 3](./images/create-iam-3.png)

Create the role. This role will be assigned during creation of lambda functions.

To Enable the communication from this static page to our lambda functions, we need to change the configuration in every lambda function.

![Edit Configuration](./images/edit-configuration.png)

![Enabling Config](./images/enabling-config.png)


After changing , it should look like this

![After cors enabling](./images/After-cors-enabling.png)
