user_stories = """
**Introduction and Role**:  
   - "You are a product owner assistant with expertise in transforming legacy PL/SQL applications into modern,
     scalable Java microservices using Domain-Driven Design (DDD) principles. 
     I have a PL/SQL codebase composed of multiple files, each containing complex business logic implemented via PL/SQL procedures, functions, and triggers."
    - Give all the triggers procedures, functions. dont exclude them from the output.

**TASK** : Analyze the entire PL/SQL code below and create **Different user stories** that capture the purpose, key operations, and intended outcomes of each distinct function,
 procedure, triggers. Each user story should include specific details such as an ID, title, requirements, description, acceptance criteria, and validations.

**PL/SQL Code**:
``` {PLSQL_CODE} ```

**Output Format**:
  The output should be in **JSON format** with the following structure:
- **User Stories**: An array of user story objects, each containing the following fields:
- **id**: A unique identifier for each user story.
- **title**: A concise title summarizing the function or feature provided by each code component.
- **requirements**: Outline any dependencies or specific requirements for this function (e.g., input data types, permissions).
- **description**: A list of statements describing the primary purpose and high-level actions of the function or procedure (e.g., "Updates account balances", "Validates customer orders").
- **acceptance_criteria**: A list of specific conditions or rules the code enforces based on its logic (e.g., input validation rules, calculations, required conditions for successful execution).
- **validations**: A list of statements describing validation checks or constraints the code applies, ensuring accuracy, data integrity, and adherence to business rules.

Each user story should focus on a single component (e.g., function, procedure, trigger) of the PL/SQL code and should follow this JSON format:

```json Format:

  "id": "Generate Unique ID eg.(001,002)",
  "title": "<title describing the code component",
  "requirements": "<dependencies or prerequisites",
  "description": ["<description statement 1", "<description statement 2", ...],
  "acceptance_criteria": ["<criteria statement 1", "<criteria statement 2", ...],
  "validations": ["<validation statement 1","<validation statement 2", ...] ```


  - Give all the triggers procedures, functions userstories. dont exclude them from the output.
   - Output should be in JSON format with the following keys: id, title,requirements, description, acceptance_criteria, validations.
   - Do not give any additional information other than the JSON ouput.
"""


userstories_microservice_prompt = """
**Role**: 
        You are a product owner assistant skilled in converting legacy PL/SQL user stories into modern, 
        scalable Java Spring Boot microservices. Your expertise includes applying Domain-Driven Design (DDD) principles to ensure modular,
        maintainable, and well-structured Java microservices.

        
**Goals and Improvements**:
  - **Enhanced Role Definition**: Added Java-centric expertise (Spring Boot, OOP) and emphasized microservice concepts.
  - **Specificity**: Incorporated object-oriented and microservice requirements for the transformation, essential for Java.
  - **Java-Specific Fields**: Added fields like API response handling and exception criteria within acceptance criteria.
  - Analyse all the PLSQL Userstories and generate into JAVA microservice userstories follwed by Requirements and steps.For each user story, 
  consolidate related PL/SQL functionalities into single cohesive microservices that align with Domain-Driven Design (DDD) principles, 
  ensuring each service follows object-oriented practices and microservice design principles. 
  
  
**Input Requirements**:
1. **Analyze the PL/SQL User Stories and Code**:  
   - **PL/SQL User Stories**: 
			```{USER_STORIES} ```
   - **PLSQL Code**: 
		```{PLSQL_CODE}```
  
- Consolidate similar PL/SQL functionalities into cohesive user stories for Java microservices.

  Examples:
   - **Example 1**: If there are procedures like `AddItem`, `RemoveItem`, `UpdateItem`, `GetItem`, and `ListItems`, these should be grouped into a single `Inventory Management` microservice user story.
   
  

Apply similar logic to organize the functionalities in cohesive, DDD-aligned Java microservices.

Follow these steps to complete the task:
1. Analyze the PLSQL code:
   a. Identify the main functionalities and business logic in the code.
   b. Determine the data structures and their relationships.
   c. Recognize any existing modules or logical separations in the code.

2. Apply Domain-Driven Design (DDD) principles:
   a. Identify the core domain and subdomains based on the business logic in the PLSQL code.
   b. Define bounded contexts for each subdomain.
   c. Identify entities, value objects, and aggregates within each bounded context.
   d. Determine the domain events and commands.

3. Design microservices:
   a. Map each bounded context to a potential microservice.
   b. Ensure each microservice has a single responsibility and is loosely coupled.
   c. Define the APIs for each microservice, including endpoints and data contracts.
   d. Identify shared libraries or common functionalities that can be extracted.

  
**Formatting**: Used JSON to maintain clarity and consistency across multiple user stories.
Follow these steps to convert the PLSQL user stories to Java/Spring Boot microservice user stories:
	1. Identify the main functionalities and data structures in the PLSQL code and userstories.
	2. Map PLSQL procedures and functions to Java methods.
	3. Convert PLSQL data types to appropriate Java data types.
	4. Replace PLSQL-specific constructs with Java equivalents.
	5. Implement database operations using Spring Data JPA or JDBC Template.
	6. Use the Exception handle by PLSQL provide equivalent type in java. 
	make use of the validation steps to conversion of PLSQL user stories to Java/Spring Boot microservice user stories Generation
 
The output should be in JSON format with the following structure:
- **User Stories**: An array of user story objects, each containing the following fields:
- **id**: A unique identifier for each user story.
- **title**: A concise title summarizing the function or feature provided by each code component.
- **requirements**:Give me the Detailed requirements, Outline any dependencies or specific requirements for this function (e.g., input data types, permissions).
- **description**: A list of statements describing the primary purpose and high-level actions of the function or procedure (e.g., "Updates account balances", "Validates customer orders").
- **acceptance_criteria**: A list of specific conditions or rules the code enforces based on its logic (e.g., input validation rules, calculations, required conditions for successful execution).
- **validations**: A list of statements describing validation checks or constraints the code applies, ensuring accuracy, data integrity, and adherence to business rules.

Each user story should focus on a single component (e.g., function, procedure, trigger) of the PL/SQL usestories and should follow this JSON format:
```json Format:

  "id": "Generate Unique ID eg.(001,002)",
  "title": "<title describing the code component",
  "requirements": "<dependencies or prerequisites",
  "description": ["<description statement 1", "<description statement 2", ...],
  "acceptance_criteria": ["<criteria statement 1", "<criteria statement 2", ...],
  "validations": ["<validation statement 1", "<validation statement 2", ...] ```


  ** Notes **:   
  
   - Output should be in JSON format with the following keys: id, title,requirements, description, acceptance_criteria, validations.
   - Do not give any additional information other than the JSON ouput.
"""

#     - Generating Specific Userstories contains all the PL/SQL similar functionality  into an single userstories 
# 	Examples : 1
#     (We have list of PL/SQL proceduer like. AddCustomers,DeleteCustomer,UpdateCustomer,GetCustomer,GetAllCustomers,make all these into the single java microservice userstories under customer class we need to get all these functionality.)
	
#     Example : 2 
#  Example : 2 
    # Consider if we have a 
    # - Employee login and Customer Login Procedures that should need to convert into single java micro-service user stories like User Authentication Service
    # - If Suppose customerAccount_library , employeeAccount_library procedures that should need to convert into single java micro-service user stories like Account Management Service
    # - If Suppose Customer and Employee CURD function that should need to convert into single java micro-service user stories like Customer and Employee CURD Services.

extract_json = """
- Your task is to identify and extract JSON objects from the provided text.
- Extract all JSON objects from the provided text. 
- Combine all extracted JSON objects into a single list **User Stories** and return only the JSON data in the following format:

Text for extraction:
```{text}```

**output Formate**:
[
   <JSON object 1,
    <JSON object 2,
    ...
    <JSON object n
]
- Do not give any additional information other than the JSON ouput.

"""

extract_oo_design_json = """
- Your task is to identify and extract Microservice design from the provided text.
- Extract all Microservice design from the provided text.

Text for extraction:
```{text}```

**output Formate**:
" <"Microservice name: A brief name for the microservice.">":  
        "Subdomain" <"Subdomain description: A brief description of the subdomain and its functionality.">,        
        "Responsibilities": <"List of responsibilities or actions handled by the microservice."> ,
        "Main Entities": <"List of main entities managed by the microservice">,
        "API Endpoints": <"HTTP Method /endpoint <parameters>": "List of API endpoints and the HTTP methods (e.g., POST, GET) with relevant parameters.">,
        "Additional Considerations": 
            <"Any additional strategies or technologies to consider such as migration, event sourcing, security, etc.">
  
- Do not give any additional information other than the JSON ouput.

"""



code_gen = """

**Goal:** Generate fully developed Java microservice code for each entity based on the given user stories, using Spring Boot and Domain-Driven Design (DDD) principles.

**Context - User Stories:** `: {user_stories}`

**Requirements:**

Generate Java/Spring Boot code for individual microservices representing each entity, fully encapsulating layers and components for a microservices architecture. Apply DDD principles to create a well-structured, object-oriented codebase. Each microservice should be self-contained, complete, and follow best practices without placeholders, omitted sections, or comments describing logic instead of actual code.

**Expected Output Structure:**

1. **Project Structure**:
   - Create a new Spring Boot project for each entity (e.g., `EmployeeService`, `BookService`), with each project structured as an independent microservice.
   - Each microservice should have separate `controller`, `service`, and `repository` packages.

2. **Layered Architecture**:
   - **Controller Layer**: For each microservice, implement a RESTful controller to handle all CRUD operations for that specific entity (e.g., `EmployeeController`, `BookController`). Include endpoints for creating, reading, updating, and deleting entities, following RESTful naming conventions and returning JSON responses.
   - **Service Layer**: Implement a service layer (e.g., `EmployeeService`, `BookService`) that fully encapsulates business logic. **Do not use comments to represent logic**; instead, write complete implementations of all functions required to fulfill the user story’s logic, such as verifying accounts, updating balances, or processing data.
   - **Data Access Layer**: Define repository interfaces (e.g., `EmployeeRepository`, `BookRepository`) using Spring Data JPA with CRUD operations and any required business logic. Each microservice should have a separate database configuration in `application.yml` or `application.properties` if necessary.

3. **Additional Requirements**:
   - **Error Handling**: Add global exception handling in each microservice for common errors (e.g., validation, not found) and configure clear HTTP status responses.
   - **Swagger Documentation**: Enable Swagger in each microservice for API endpoint documentation.
   - **Testing**: Write unit tests for service methods and integration tests for controller endpoints in each microservice, using JUnit and Mockito.
   - **Independent Packaging and Deployment**: Package each microservice as an independent JAR with an embedded Tomcat server (e.g., `java -jar <filename>.jar`). Each microservice should be independently deployable and communicate over HTTP if future inter-service communication is needed.

4. **Output Format**:
   - **Java Code**:
     - `usecase`: Briefly describe the user story for the entity.
     - Include package declarations, imports, class declarations, and **fully implemented CRUD methods and any additional logic required**, avoiding placeholder comments. Ensure all necessary CRUD functions are provided for a complete solution.
   - **File Structure**:
     - Java files organized by DDD layers (Model, Repository, Service, Controller).
   - **Completion Indicator**: End response with "*END*" for clarity.


**Restrictions:**

- **Output**: Java code only, without additional text.
- **Completeness**: No placeholders or incomplete methods. All functions should contain complete logic implementations to fulfill the user stories.
- **Formatting**: Use `@Data` from Lombok for getters/setters if applicable.
- **Token Limit**: Ignore. Generate full responses; follow up with additional calls if incomplete.


"""

# oo_design_prompt_plus = """
# **Role**:  
# You are an experienced software engineer specializing in **Domain-Driven Design (DDD)** and **microservices architecture**. 
# Your expertise will help modernize a complex legacy PLSQL codebase into modern Java and Spring Boot-based microservices.

# ---

# **Objective**:  
# - Your primary goal is to analyze the provided PLSQL code and translate it into a modular, object-oriented design using **DDD principles** and implement it as **microservices**.  
# - The final design should focus on **maintainability, scalability**, and **flexibility**.  

# ---

# **Steps to Complete the Task**

#  1. **Analyze the PLSQL Code**:  
#    - **Identify Functionalities**: Review the business logic implemented in the PLSQL code.  
#    - **Determine Data Structures**: Extract data structures, tables, and their relationships.  
#    - **Logical Modules**: Recognize any existing modular separations in the PLSQL logic that can inform domain boundaries.  

#  2. **Apply Domain-Driven Design (DDD) Principles**:  
#    - **Core Domain & Subdomains**: Identify the **core domain** and any related **subdomains** from the business logic.  
#    - **Bounded Contexts**: Define **bounded contexts** for each subdomain.  
#    - **Key Concepts**: Identify **entities**, **value objects**, and **aggregates** within each context.  
#    - **Domain Events & Commands**: Determine the events and commands necessary for the interactions between bounded contexts.  

# 3. **Design Microservices**:  
#    - **Map Bounded Contexts to Microservices**: Each bounded context should map to one or more microservices.  
#    - **Responsibilities**: Ensure each microservice has a **single responsibility** and is **loosely coupled**.  
#    - **Define APIs**:  
#      - Describe REST endpoints for each microservice.  
#      - Define the **input/output data contracts** and payloads.  
#    - **Shared Libraries**: Identify functionalities that can be extracted into shared libraries for reusability.  

#  4. **Output Format**:  
# Provide your output in the following structured format:  

# ```plaintext
# <answer>
# Overview of Identified Domains and Subdomains
# [Provide a brief summary of the core domain and subdomains.]

# Microservices Design :
# 1. **Microservice Name**: [Name of the microservice]  
#    - **Responsibilities**: [Briefly describe its main responsibilities.]  
#    - **Key Entities**: [List key entities and their relationships.]  
#    - **Aggregates**: [Describe the aggregates within the service.]  
#    - **Bounded Context**: [Explain its bounded context.]  
   
#    **APIs**:  
#    - **Endpoint**: [API endpoint URL and method.]  
#      - **Request Body**: [Define the input structure.]  
#      - **Response Body**: [Define the output structure.]  

# [Repeat for each microservice.]

# ### Shared Libraries and Utilities
# [List any shared components or libraries and their responsibilities.]

# ### Additional Considerations
# [Provide recommendations for data migration, handling transactions, deployment strategies, or any edge cases.]

# **END**
# </answer>
# ```



# **Requirements**:  
# 1. **Comprehensive Analysis**: Fully analyze the PLSQL code to extract all relevant details for the new design.  
# 2. **Accuracy**: Ensure that the DDD principles (domains, contexts, entities, etc.) are clearly reflected in the design.  
# 3. **API Details**: Clearly define endpoints, payloads, and data formats for each microservice.  
# 4. **Well-Structured Output**: Follow the specified output format to ensure clarity and completeness.  



# **Additional Guidelines**:  
# 1. **Prioritize Modularity**: Break down large functionalities into smaller, self-contained microservices.  
# 2. **Avoid Over-Engineering**: Only create shared libraries or utilities where truly necessary.  
# 3. **Validation**: Ensure the output is complete and adheres to the format.  
# 4. **Domain-Focused Design**: Keep the focus on aligning microservices with business processes and logical domains.  



# **Restrictions**:  
# - Adhere strictly to the output format enclosed in `<answer>` tags.  
# - Provide all four requirements explicitly for every microservice.  
# - Output the word **END** at the end of your response to indicate completion.  


# """


oo_design_prompt_plus = """

**Role**:
   - You are an experienced software engineer specializing in Domain-Driven Design (DDD) and microservices architecture.
   - You are tasked with modernizing a complex legacy PLSQL codebase to modern Java and Spring Boot microservices. 

** Goal**:
   Your goal is to generate an object-oriented design from the PLSQL code using Domain-Driven Design (DDD) principles to break the 
design into microservices. 

**INPUT** : 

Here is the PLSQL code you need to analyze:

```
<plsql_code>
    {PLSQL_CODE}
</plsql_code>
```

**Requirements:**
Follow these steps to complete the task:

1. Analyze the PLSQL code:
   a. Identify the main functionalities and business logic in the code.
   b. Determine the data structures and their relationships.
   c. Recognize any existing modules or logical separations in the code.

2. Apply Domain-Driven Design (DDD) principles:
   a. Identify the core domain and subdomains based on the business logic in the PLSQL code.
   b. Define bounded contexts for each subdomain.
   c. Identify entities, value objects, and aggregates within each bounded context.
   d. Determine the domain events and commands.

3. Design microservices:
   a. Map each bounded context to a potential microservice.
   b. Ensure each microservice has a one or two responsibility and is loosely coupled.
   c. Define the APIs for each microservice, including endpoints and data contracts.
   d. Identify shared libraries or common functionalities that can be extracted.
   

4. Provide your output in the following format:
   a. Start with a brief overview of the identified domains and subdomains.
   b. List each microservice with its responsibilities and main entities.
   c. Describe the APIs for each microservice.
   d. Conclude with any additional considerations or recommendations for the modernization process.

**Restrictions:**
Ensure to generate all four requirements for the above format.
Remember to focus on creating a clean, modular design that adheres to DDD principles and microservices architecture 
best practices. Your design should aim to improve maintainability, scalability, and flexibility compared to the original
PLSQL codebase.
 

"""



userstories_mapping_prompt ="""

**Role**:  
- You are a JSON generator responsible for mapping user stories to microservices based on their design, responsibilities, entities, and APIs.  
- Analyse the use stories and match them to the microservices in the provided design.

**Task**:  
I will provide a **Microservice Design** and a list of **User Stories**.  
Your responsibilities are:  
1. **Analyze the Microservice Design and User Stories**: Carefully read and understand the purpose, responsibilities, entities, and APIs of each microservice.  
2. **Map User Stories**: Match each user story to its corresponding microservice based on its scope, functionality, and relevance to the microservice's design.  
3. **Categorize Unmapped Stories**: If a user story does not align with any microservice, categorize it under a special key:  
   `"Additionalmicroservice - userstories[Unmapped Stories]"`.  
4. **Generate a Strict JSON Output**: Follow a strict JSON syntax with no errors in formatting or content.  

**Input**:  
- **Microservice Design**: {microservice_design}  
- **User Stories**: {user_stories}  

**Output Format**: 
```json

  "<Microservice Name>": [
    "<user story id",
    "<user story id>",
    "...",
    "<user story id>"
  ],
  "Additionalmicroservice - userstories[Unmapped Stories]": [
    "<user story id>",
    "..."
  ]

``` 

```json

  "<Microservice Name>": [
    "<Complete user story with all details>",
    "<user story 2>",
    "...",
    "<user story n>"
  ],
  "Additionalmicroservice - userstories[Unmapped Stories]": [
    "<user story>",
    "..."
  ]

```


**Requirements**:  
1. **Accuracy**: Map user stories to microservices based on their design, responsibilities, entities, and APIs.  
2. **Clarity**: Ensure that each story is placed in the most relevant microservice.  
3. **Handling Edge Cases**: Place unmapped user stories under `"Additionalmicroservice - userstories[Unmapped Stories]"`.  
4. **Validation**: Ensure that the JSON output is valid and well-structured with no missing commas, brackets, or keys.  

**Steps to Ensure Accuracy**:  
1. **Understand Microservice Design**: Break down each microservice's purpose, entities, and API functionalities.  
2. **Analyze User Stories**: Identify keywords and functionality within each story to match it to the appropriate microservice.  
3. **Iterative Matching**: Go through each user story one by one, comparing it to each microservice design.  
4. **Fallback for Unmapped Stories**: For stories that cannot be mapped, add them to the `"Additionalmicroservice - userstories[Unmapped Stories]"` category.  

**Guidelines for Output**:  
- The JSON structure must include **all microservices** explicitly, even if they do not have any user stories.  
- Include the full details of each user story under the appropriate key.  
- Use proper indentation for JSON readability.  

**Restrictions**:  
- Output must be strictly in JSON format with correct syntax.  
- Do not skip or combine user stories without explicitly categorizing them.  
- Ensure no microservices or user stories are omitted.


"""

# userstories_mapping_prompt = """

# **Role**:  
# - You are also a JSON generator responsible for organizing user stories based on the provided microservice design. 
# - Your task is to map user stories to their corresponding microservices based on their responsibilities ,design,entities and api.    

# **Task**:  
# I will provide a **Microservice Design** and a list of **User Stories**. 
# Your responsibilities are:  
# First Analyse the Microservice Design and User Stories and then
# 1. Match each user story to its corresponding microservice based on the microservice's responsibilities ,design,entities and api.  
# 2. If a user story does not align with any microservice, categorize it under the key:  
#    **"Additionalmicroservice - userstories[Unmapped Stories]"**.  

# **Input**:  
# Microservice Design: {microservice_design}  
# User Stories: {user_stories}  

# **Output Format**:  
# Generate a JSON object in the following format:  

#   "<Complete microservice design>": ["<Complete user story with all details>", "<user story 2>", ..."<user story n>"],
#   "Additionalmicroservice - userstories[Unmapped Stories]": ["<user story>", ...]


# **Requirements**:  
# 1. Match user stories accurately to their microservices.  
# 2. Handle unmapped user stories by categorizing them under the `"Additionalmicroservice - userstories[Unmapped Stories]"` key.  
# 3. Ensure output follows strict JSON syntax.

# **Restrictions:**
# output should be in the json format
# """


javacode_prompt = """
** Role ** :  
Generate a Java microservice application based on the following microservice design and user stories in JSON format. 
The application should be structured according to microservices principles, with clear separation of concerns, appropriate service layers, and API endpoints. 
Each user story should be implemented as a separate feature or module in the application. Ensure the following:

- Use Spring Boot for the microservices framework.
- Follow Domain-Driven Design (DDD) principles for code organization.
- Implement RESTful APIs for each microservice.
- Ensure scalability, performance, and security best practices.
- Handle exceptions, validation, and logging properly.
- Provide a sample JSON request/response for each user story.
- Ensure unit tests are written for each feature.


Microservice Design:  
```
{microservice_design}```

User Stories:  
```
{userstories}
```

"""

