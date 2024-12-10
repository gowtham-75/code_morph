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
  The output should be in JSON format with the following structure:
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
  "validations": ["<validation statement 1", "<validation statement 2", ...] ```


  - Give all the triggers procedures, functions userstories. dont exclude them from the output.
   - Output should be in JSON format with the following keys: id, title,requirements, description, acceptance_criteria, validations.
   - Do not give any additional information other than the JSON ouput.
"""


userstories_microservice_prompt = """
**Role**: 
        You are a product owner assistant skilled in converting legacy PL/SQL user stories into modern, 
        scalable Java Spring Boot microservices. Your expertise includes applying Domain-Driven Design (DDD) principles to ensure modular,
        maintainable, and well-structured Java microservices

        
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
   - **Example 2**: If there are procedures for different types of reporting such as `GenerateSalesReport`, `GenerateInventoryReport`, and `GenerateRevenueReport`, consolidate them into a single `Reporting Service`.
   - **Example 3**: If there are various CRUD operations for entities like `Order` and `Customer`, group them under `Order Management` and `Customer Management` microservices, respectively.

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



# code_gen_0_1= """

# **Goal:** Generate a fully developed Java microservice code for each entity based on the given user stories, using Spring Boot and Domain-Driven Design (DDD) principles.


# **Context - User Stories:** `: {user_stories}`

# **Requirements:**

# Generate Java/Spring Boot code for individual microservices representing each entity, fully encapsulating layers and components for a microservices architecture. Apply DDD principles to create a well-structured, object-oriented codebase. Each microservice should be self-contained, complete, and follow best practices without placeholders, omitted sections, or comments describing logic instead of actual code.

# **Expected Output Structure:**

# 1. **Project Structure**:
#    - Create a new Spring Boot project for each entity (e.g., `EmployeeService`, `BookService`), with each project structured as an independent microservice.
#    - Each microservice should have separate `controller`, `service`, and `repository` packages.

# 2. **Layered Architecture**:
#    - **Controller Layer**: For each microservice, implement a RESTful controller to handle CRUD operations for that specific entity (e.g., `EmployeeController`, `BookController`), exposing endpoints that follow RESTful naming conventions and return JSON responses.
#    - **Service Layer**: Implement a service layer (e.g., `EmployeeService`, `BookService`) that fully encapsulates business logic. **Do not use comments to represent logic**; instead, write complete implementations of all functions required to fulfill the user story’s logic, such as verifying accounts, updating balances, or processing data.
#    - **Data Access Layer**: Define repository interfaces (e.g., `EmployeeRepository`, `BookRepository`) using Spring Data JPA with CRUD operations and any required business logic. Each microservice should have a separate database configuration in `application.yml` or `application.properties` if necessary.

# 3. **Additional Requirements**:
#    - **Error Handling**: Add global exception handling in each microservice for common errors (e.g., validation, not found) and configure clear HTTP status responses.
#    - **Swagger Documentation**: Enable Swagger in each microservice for API endpoint documentation.
#    - **Testing**: Write unit tests for service methods and integration tests for controller endpoints in each microservice, using JUnit and Mockito.
#    - **Independent Packaging and Deployment**: Package each microservice as an independent JAR with an embedded Tomcat server (e.g., `java -jar <filename>.jar`). Each microservice should be independently deployable and communicate over HTTP if future inter-service communication is needed.

# 4. **Output Format**:
#    - **Java Code**:
#      - `usecase`: Briefly describe the user story for the entity.
#      - Include package declarations, imports, class declarations, and full method implementations with business logic and  **fully implemented CRUD methods and any additional logic required**, avoiding placeholder comments. Ensure all necessary CRUD functions are provided for a complete solution.
#    - **File Structure**:
#      - Java files organized by DDD layers (Model, Repository, Service, Controller).
#    - **Completion Indicator**: End response with "*END*" for clarity.


# **Restrictions:**

# - **Output**: Java code only, without additional text.
# - **Completeness**: No placeholders or incomplete methods. All functions should contain complete logic implementations to fulfill the user stories.
# - **Formatting**: Use `@Data` from Lombok for getters/setters if applicable.
# - **Token Limit**: Ignore. Generate full responses; follow up with additional calls if incomplete.



# """



# code_gen_updated="""



# **Goal:** Generate a fully developed Java microservice code for each entity based on the given user stories, 
# using Spring Boot and Domain-Driven Design (DDD) principles.
# **Context-User Stories:** ` : {user_stories}` 
# **Requirements:**
# Generate Java/Spring Boot code for individual microservices representing each entity, fully encapsulating layers and components for a microservices architecture. Apply DDD principles to create a well-structured, object-oriented codebase. Each microservice should be self-contained, complete, and follow best practices without placeholders or omitted sections.

# **Expected Output Structure:**
# 1. **Project Structure**:
#    - Create a new Spring Boot project for each entity (e.g., `EmployeeService`, `BookService`), with each project structured as an independent microservice.
#    - Each microservice should have separate `controller`, `service`, and `repository` packages.

# 2. **Layered Architecture**:
#    - **Controller Layer**: For each microservice, implement a RESTful controller to handle CRUD operations for that specific entity (e.g., `EmployeeController`, `BookController`), exposing endpoints that follow RESTful naming conventions and return JSON responses.
#    - **Service Layer**: Implement a service layer (e.g., `EmployeeService`, `BookService`) for encapsulating business logic.
#    - **Data Access Layer**: Define repository interfaces (e.g., `EmployeeRepository`, `BookRepository`) using Spring Data JPA with CRUD operations and any required business logic. Each microservice should have a separate database configuration in `application.yml` or `application.properties` if necessary.

# 3. **Additional Requirements**:
#    - **Error Handling**: Add global exception handling in each microservice for common errors (e.g., validation, not found) and configure clear HTTP status responses.
#    - **Swagger Documentation**: Enable Swagger in each microservice for API endpoint documentation.
#    - **Testing**: Write unit tests for service methods and integration tests for controller endpoints in each microservice, using JUnit and Mockito.
#    - **Independent Packaging and Deployment**: Package each microservice as an independent JAR with an embedded Tomcat server (e.g., `java -jar <filename>.jar`). Each microservice should be independently deployable and communicate over HTTP if future inter-service communication is needed.

# 4. **Output Format**:
#    - **Java Code**:
#      - `usecase`: Briefly describe the user story for the entity.
#      - Include package declarations, imports, class declarations, and method implementations with comments for each component.
#    - **File Structure**:
#      - Java files organized by DDD layers (Model, Repository, Service, Controller).
#    - **Completion Indicator**: End response with "*END*" for clarity.



# **Restrictions:**
# - **Output**: Java code only, without additional text.
# - **Completeness**: No placeholders. Generate complete code for each part.
# - **Formatting**: Use `@Data` from Lombok for getters/setters if applicable.
# - **Token Limit**: Ignore. Generate full responses; follow up with additional calls if incomplete.


# """
# # code_gen2="""

# # **Goal:** Generate a fully developed Java microservice code for the given user stories using Spring Boot and Domain-Driven Design (DDD).

# # **Context:** UserStories : {user_stories}

# # **Requirements:**

# # Generate Java/Spring Boot code with all essential layers and components in a microservices architecture. Follow DDD principles to create a well-structured, object-oriented codebase. Ensure output is comprehensive, without placeholders or omitted sections.

# # **Expected Output Structure:**

# # 1. **Code Structure**:
# #    - For each user story:
# #      - **Model**: Define entity classes with fields and annotations.
# #      - **Repository**: Create interfaces for CRUD operations.
# #      - **Service**: Implement business logic and validations.
# #      - **Controller**: Develop API endpoints (e.g., `GET`, `POST`, `PUT`, `DELETE`).
# #      - **Exception Handling**: Global exception handling for HTTP status management.
# #      - **DTOs** (optional): For request/response structures if necessary.
# #      - **Database Configuration**: Include basic MySQL configuration in `application.properties`.
# #      - **API Documentation**: Sample requests/responses for each endpoint.

# # 2. **Output Format**:
# #    - **Java Code**:
# #      - `usecase`: Briefly describe the user story.
# #      - Include package declarations, imports, class declarations, method implementations, and comments for each component.
# #    - **File Structure**:
# #      - Java files organized by DDD layers (Model, Repository, Service, Controller).
# #    - **Completion Indicator**: End response with "*END*" for clarity.

# # **Restrictions:**

# # - **Output**: Java code only, without additional text.
# # - **Completeness**: No placeholders. Generate complete code for each part.
# # - **Formatting**: Use `@Data` from Lombok for getters/setters if applicable.
# # - **Token Limit**: Ignore. Generate full responses; follow up with additional calls if incomplete.


# """

# # code_gen1 = """

# You are a specialized converter for userstories into a modern Java/Spring Boot microservices architecture using Domain-Driven Design (DDD) principles. Your task is to fully convert the given userstories into a comprehensive and well-structured Java/Spring Boot application. The output should include all essential components, ensuring a complete codebase with no placeholders or partial code.
# You are tasked with generating Java/Spring Boot microservice code , modernizing it into a architecture using Domain-Driven Design (DDD) concepts.
# Your goal is to create a fully object-oriented codebase that is well-structured and follows best practices for Spring Boot applications. 
# Dont omitte anything for brevity and do not give any additional information other than the Java code.Try to generate the complete code response with proper mapping of other microservices.

# UserStories : {user_stories}

#  - **Instructions:**
#    - For each user story provided, create the necessary components of a microservice including:
#      - **Model**: Define entity models with appropriate fields.
#      - **Repository**: Create repository interfaces for CRUD operations based on the model.
#      - **Service**: Implement service classes that handle business logic, validation, and database interactions.
#      - **Controller**: Develop RESTful API endpoints that fulfill the user story requirements, with HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`.
#      - **Exception Handling**: Implement global exception handling to manage errors and return relevant HTTP status codes based on the user stories’ acceptance criteria.
#      - **DTOs** (Data Transfer Objects) if needed: For handling request and response objects.
#    - **Database Configuration**: Include a basic configuration in `application.properties` for a MySQL database.
#    - **API Documentation**: Provide sample API requests and responses for each endpoint, with success and error scenarios.


#  - **Expected Output**:
#    - End-to-end Java Spring Boot code that satisfies each user story’s requirements and acceptance criteria.
#    - Classes for `Model`, `Repository`, `Service`, `Controller`, and `Exception Handler` as needed.
#    **NOTE**: generate only java code. Do not give any additional information other than the Java code.
   
#   **Output Formate**:
#   usecase : Name of the usecase
#  ```java
 
 
# Package declaration
# package com.example.microservice.[layer];
 
# Import statements
 
# Class declarations, including annotations
 
# Method implementations with comments explaining functionality
 
# ```

# Your final output should include multiple Java files representing the different components of the microservices
# architecture, along with a brief explanation of how the code is organized and how it implements the DDD concepts.
 
# Please also output the word *END* at the end of your response to indicate completion.
 
# Instruction for the Generate complete long response output:
#    Dont give like Other methods for updating, Other endpoints instead of generate complete code,instead of generating constructor ,Getters and setters give the lambok.
#    eg : ```// Getters and setters omitted for brevity ,
#         // Constructors, Getters, Setters, HashCode and Equals methods
#     // Omitted for brevity```
#    we need to generate the complete code based on the user stories.
#    we have more than one LLM calls are availbale.
#    Everytime try to generate the complete code.
#    Dont provide the incomplete code.
#    Dont worried about the within token limit try to generate. I need a complete code generate.
#    If Incomplete response based on that it will generate the code in next call.


# """


 
 


#  - **Instructions:**
#    - For each user story provided, create the necessary components of a microservice including:
#      - **Model**: Define entity models with appropriate fields.
#      - **Repository**: Create repository interfaces for CRUD operations based on the model.
#      - **Service**: Implement service classes that handle business logic, validation, and database interactions.
#      - **Controller**: Develop RESTful API endpoints that fulfill the user story requirements, with HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`.
#      - **Exception Handling**: Implement global exception handling to manage errors and return relevant HTTP status codes based on the user stories’ acceptance criteria.
#      - **DTOs** (Data Transfer Objects) if needed: For handling request and response objects.
#    - **Database Configuration**: Include a basic configuration in `application.properties` for a MySQL database.
#    - **API Documentation**: Provide sample API requests and responses for each endpoint, with success and error scenarios.


#  - **Expected Output**:
#    - End-to-end Java Spring Boot code that satisfies each user story’s requirements and acceptance criteria.
#    - Classes for `Model`, `Repository`, `Service`, `Controller`, and `Exception Handler` as needed.




#- ----------- userstories -------------------------------
# **Introduction and Role**:  
#    - "You are a software engineering assistant with expertise in transforming legacy PL/SQL applications into modern,
#      scalable Java microservices using Domain-Driven Design (DDD) principles. 
#      I have a PL/SQL codebase composed of multiple files, each containing complex business logic implemented via PL/SQL procedures, functions, and triggers."

# **TASK** : Analyze the entire PL/SQL code below and create **Different user stories** that capture the purpose, key operations, and intended outcomes of each distinct function,
#  procedure, or trigger. Each user story should include specific details such as an ID, title, requirements, description, acceptance criteria, and validations.

# **PL/SQL Code**:
# ``` {PLSQL_CODE} ```

#   The output should be in JSON format with the following structure:
# - **User Stories**: An array of user story objects, each containing the following fields:
# - **id**: A unique identifier for each user story.
# - **title**: A concise title summarizing the function or feature provided by each code component.
# - **requirements**: Outline any dependencies or specific requirements for this function (e.g., input data types, permissions).
# - **description**: A list of statements describing the primary purpose and high-level actions of the function or procedure (e.g., "Updates account balances", "Validates customer orders").
# - **acceptance_criteria**: A list of specific conditions or rules the code enforces based on its logic (e.g., input validation rules, calculations, required conditions for successful execution).
# - **validations**: A list of statements describing validation checks or constraints the code applies, ensuring accuracy, data integrity, and adherence to business rules.

# Each user story should focus on a single component (e.g., function, procedure, trigger) of the PL/SQL code and should follow this JSON format:

# ```json Format:

#   "id": "Generate Unique ID eg.(001,002)",
#   "title": "<title describing the code component",
#   "requirements": "<dependencies or prerequisites",
#   "description": ["<description statement 1", "<description statement 2", ...],
#   "acceptance_criteria": ["<criteria statement 1", "<criteria statement 2", ...],
#   "validations": ["<validation statement 1", "<validation statement 2", ...] ```



#    - Output should be in JSON format with the following keys: id, title,requirements, description, acceptance_criteria, validations.
#    - Do not give any additional information other than the JSON ouput.