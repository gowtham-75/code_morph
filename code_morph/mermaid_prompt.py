mermaid_code_generate= """
            Create a Mermaid diagram of type diagram type : {UML_DIAGRAM} for the provided data. Your task is to generate the Mermaid code block that represents the described diagram.
            For the given code : {PLSQL_CODE} model class generate the proper Marmaid code for the diagram_type.
 
            Instruction must need to follow or else diagram cant able to generate:
            -Do not include any description, do not include the \`\`\`.
            -Correct generated mermaid code if any syntax error present.
            -Do not include any BLOCK STOPS
            -Do not include any COMMAS
            -Strictly generate mermaid code for entire input.
            -Please make sure, only the Mermaid code block is required without any additional descriptions or code block delimiters.
           
            - If word could be 'cart item','belongs to' means dont give space in-between need to mention as 'cartItem', 'belongsto'
            - except the sequence diagram in mermaid code strictly dont include >>, <<, >, <. if tag will be there it wont generate the diagrams.
            - strictly Dont include back ticks ``` and mermain in the output.
            - Field must contains single colon only more then will remove it.
            - If class diagram contains empty class means Strictly dont add in the mermind generating code. like class ProductNotFoundException  class ProductRepository  class SpringBootApplications
            - dont include the Angle brackets,tags like <, >, >>, << List<Product>, Optional<Product>, ResponseEntity<Product>, <<SpringBootApplication>>, ResponseEntity<String>, ResponseEntity<?>. please dont include any open tag or close tag, Greater than sign or Less than sign  
            - In flowchart TD Dont include '()' this kind of brackets. If include in code it wont generete diagramtic output.
                """
class_diagram = """
Generate a {UML_DIAGRAM}  based on the provided PL/SQL model class code, stored in `{PLSQL_CODE}`. Follow these strict specifications:
- You are recognized as an expert in generating Mermaid diagrams. Based on the PL/SQL code provided, your task is to create a Mermaid {UML_DIAGRAM} diagram that fully represents the structure and relationships as specified above.
- Please provide the complete Mermaid code for this {UML_DIAGRAM} diagram. 
- Ensure that the output consists solely of the Mermaid code; do not include any additional text, comments, or explanations in the output.
- Verify that the generated Mermaid code is valid and can be rendered accurately without any errors.

1. **Relationship Symbols:**
   - Use `<|--` for inheritance.
   - Use `*--` for composition.
   - Use `o--` for aggregation.
   - Use `-->` for association.
   - Use `--` for a solid link.
   - Use `..>` for dependency.
   - Use `..|>` for realization.
   - Use `..` for a dashed link.
   - Use `<|--|>` for bidirectional inheritance.
   - Use `--|>` for labeled inheritance (e.g., `--|> classB : Inheritance`).
   - Use `--*` for labeled composition.
   - Use `--o` for labeled aggregation.
   - Use `-->` for labeled association.

2. **Class Annotations:**
   - Use `<<Interface>>` for interfaces.
   - Use `<<Abstract>>` for abstract classes.
   - Use `<<Service>>` for service classes.
   - Use `<<Enumeration>>` for enums.

3. **Class Definitions:**
   - Format classes using `class ClassName` and list members inside.
   - Use `+` for public, `-` for private, `#` for protected, and `~` for package/internal visibility.
   - For methods, specify return types (e.g., `+methodName() : returnType`) without repeating colons on a single line.

4. **Additional Notes:**
   - Use `note "Your note here"` for general notes.
   - Use `note for <CLASS NAME> "Your note here"` to add a note specific to a class.
   - Define namespaces with `namespace NamespaceName` to group related classes.
   - **Do not include** the note in the code

5. **Syntax Requirements:**
   - **Strictly avoid** using unsupported symbols, special characters, or double colons in a single line, including inside brackets (e.g., `(10 2)` instead of `(10:2)`).
   - Use alphanumeric characters, underscores, and dashes only for class names.
   - Ensure the Mermaid code is valid and error-free without any unsupported elements like angle brackets `< >`, nested colons `::`, or list types such as `List<String>`.



"""

class_diagram2= """
   Your objective is to create a comprehensive and detailed Mermaid diagram of type {UML_DIAGRAM} based on the provided data. This task involves generating a precise and syntactically correct Mermaid code block that accurately represents a class diagram derived from the supplied PL/SQL code: {PLSQL_CODE}. It is imperative that you strictly adhere to the following specifications:

1. **Relationships**: 
   In the context of the class diagram, various types of relationships between classes must be represented using the following symbols:
   - **Inheritance**: Indicated by `<|--`, which shows that one class (the child) derives from another class (the parent).
   - **Composition**: Use `*--`, signifying a strong ownership relationship where the child cannot exist independently of the parent class.
   - **Aggregation**: Represented by `o--`, indicating a relationship where the child class can exist independently of the parent class.
   - **Association**: Use `-->`, which depicts a general link between classes without implying ownership.
   - **Solid Links**: Use `--`, representing a direct connection between two classes without further qualifications.
   - **Dependency**: Indicated by `..>`, meaning one class depends on another class for its functionality.
   - **Realization**: Use `..|>`, showing that a class implements an interface.
   - **Dashed Links**: Represented by `..`, indicating a non-solid or weaker connection.
   - **Two-way Inheritance**: Use `<|--|>`, which signifies a bidirectional inheritance relationship between classes.
   - **Labeled Inheritance and Composition**: Use `--|>` for labeled inheritance and `--*` for labeled composition to clarify the nature of these relationships further.
   - **Labeled Aggregation**: Use `--o` to denote labeled aggregation relationships, providing additional context.

2. **Annotations**: 
   Annotations are crucial for clarifying the nature and purpose of classes within the diagram. Use the following notations:
   - `<<Interface>>` to denote interface classes.
   - `<<Abstract>>` for abstract classes that cannot be instantiated.
   - `<<Service>>` for service classes that typically contain business logic.
   - `<<Enumeration>>` for enumerated types that define a set of named constants.

3. **Class Definitions**: 
   When defining classes, follow these guidelines closely:
   - Use the format `class ClassName` to declare a class.
   - For class members, denote visibility using the following symbols:
     - `+` for public members (accessible from outside the class)
     - `-` for private members (accessible only within the class)
     - `#` for protected members (accessible within the class and subclasses)
     - `~` for package visibility (accessible only within the same package)
   - When specifying methods, ensure that return types are included appropriately in the format (e.g., use `+methodName() : returnType`), ensuring that only one colon appears per line.

4. **Notes**: 
   Including notes can provide essential context or clarification regarding classes and their relationships. Use the following formats:
   - For general notes applicable to the entire diagram, use `note "Your note here"`.
   - For class-specific notes that provide insight into a particular class, use `note for ClassName "Your note here"`, ensuring that the note is relevant and informative.

5. **Namespaces**: 
   To effectively organize related classes, utilize the `namespace NamespaceName` construct, which groups classes that belong to a specific context or module. This aids in maintaining a structured and readable diagram.

6. **Formatting Rules**: 
   Adhere to these critical formatting rules to ensure that the Mermaid code is syntactically correct and valid:
   - Ensure that the generated code complies with valid Mermaid syntax and avoids any unsupported characters.
   - Class names must consist solely of alphanumeric characters, underscores, and dashes to avoid rendering issues.
   - Do not include any extraneous descriptions, block stops, or commas within the code block.
   - Avoid using special symbols such as `>>`, `<<`, `>`, `<`, or any language-specific tags (e.g., `List<String>`,`<<Exception>>`,`<<Enumeration>>`) that may confuse the parser.
   - Ensure that there is only one colon per line, including within brackets; for instance, format as `User : +UserID INT` instead of `User : +UserID: INT`.
   - Ensure that no more than one colon appears on any given line.
   - While generating the mermaid code it wont generate the note 
   (eg - note "Utility class for order operations" for OrderUtils,note "Represents an order and its related information" for Order
    note "Represents a line item in an order" for LineItem
    note "Defines custom exceptions for validation and process control" for Exceptions
    note "Represents a customer with loyalty and address details" for Customer
    note "Represents a product with stock and pricing details" for Product
    note "Represents a coupon with discount details and validity" for Coupon)

- You are recognized as an expert in generating Mermaid diagrams. Based on the PL/SQL code provided, your task is to create a Mermaid {UML_DIAGRAM} diagram that fully represents the structure and relationships as specified above.
- Please provide the complete Mermaid code for this {UML_DIAGRAM} diagram. 
- Ensure that the output consists solely of the Mermaid code; do not include any additional text, comments, or explanations in the output.
- Verify that the generated Mermaid code is valid and can be rendered accurately without any errors.
"""





class_diagram1="""
- You are recognized as an expert in generating Mermaid diagrams. Based on the PL/SQL code provided, your task is to create a Mermaid {UML_DIAGRAM} diagram that fully represents the structure and relationships as specified above.
- Please provide the complete Mermaid code for this {UML_DIAGRAM} diagram. 
- Ensure that the output consists solely of the Mermaid code; do not include any additional text, comments, or explanations in the output.
- Verify that the generated Mermaid code is valid and can be rendered accurately without any errors.
Create a Mermaid diagram of type {UML_DIAGRAM} for the provided data. Your task is to generate the Mermaid code block that represents the class diagram.
For the given {PLSQL_CODE} model class generate the proper Marmaid code for the diagram_type.
   
This are the Symbols use to generate the mermaid code and avoid other than symbols.
 
Generate a Mermaid class diagram with the following specifications:
1. Use the following symbols for relationships between classes:
   - `<|--` for inheritance
   - `*--` for composition
   - `o--` for aggregation
   - `-->` for association
   - `--` for solid link
   - `..>` for dependency
   - `..|>` for realization
   - `..` for dashed link
   - `<|--|>` for two-way inheritance (bidirectional)
   - `--|>` for inheritance with a label (e.g., `--|> classB : Inheritance`)
   - `--*` for composition with a label
   - `--o` for aggregation with a label
   - `-->` for association with a label
2. Use the following annotations to add additional metadata to classes:
   - `<<Interface>>` to denote an interface
   - `<<Abstract>>` to denote an abstract class
   - `<<Service>>` to denote a service class
   - `<<Enumeration>>` to denote an enum class
3. Use labels on relationships to describe the nature of the relationship, e.g., `classA --|> classB : Inheritance`.
4. Use the following format for defining classes:
   - Class members such as attributes and methods should be listed inside the class using `class ClassName`.
   - Use `+` for public, `-` for private, `#` for protected, and `~` for package/internal visibility.
   - Methods can include return types, e.g., `+methodName() : returnType`. Please do not add more than one colon : in a single line. if added meand would not generate the mermaid class diagram.
5. You can include notes and annotations using the following:
   - `note "Your note here"` for general notes.
   - `note for <CLASS NAME> "Your note here"` to add a note for a specific class.
6. When defining a namespace, use `namespace NamespaceName ` to group related classes.
7. Ensure the Mermaid code is valid and will render correctly.
8. Avoid using any unsupported special characters or symbols that are not specified here.
9. Use alphanumeric characters, underscores, and dashes for class names.
 
Strictly follow the specification symbols and Provide the Mermaid code as the output.    
   
   Instruction must need to follow to generate the proper mermaid code class diagram:
      - Do not include any description, do not include the \`\`\`.
      - Correct generated mermaid code if any syntax error present.
      - Do not include any BLOCK STOPS and Do not include any COMMAS
      - except the sequence diagram in mermaid code strictly dont include >>, <<, >, <. if tag will be there it wont generate the diagrams.
      - dont include the Angle brackets,tags like <, >, >>, << List<String>, Optional<String>, ResponseEntity<String>, << >>, ResponseEntity<String>, ResponseEntity<?>. please dont include any open tag or close tag, Greater than sign or Less than sign.
      - Strictly Avoid double time colon will come in sigle line.. like "User : +UserID: INT" instead of "User : +UserID INT", "Room : +PricePerNight: DECIMAL(10: 2)" instead of "Room : +PricePerNight: DECIMAL(10, 2)" Dont use like two colon in single line, Inside the brackets also wont add the colons.
      - Include only once colon ":" in the line. not more that one colon in the line
      - Strictly Do not add more than one colon in the single line. If inside the bracket also must would not include the colon.
      - Please do not add more than one colon ':' in a single line must not include inside the bracket also like (10 : 8) instead of (10 8). if added meand would not generate the mermaid class diagram.
     
"""

sequence_diagram = """Create a Mermaid diagram of type {UML_DIAGRAM} for the provided data. Your task is to generate the Mermaid code block that represents the sequence diagram. For the given {PLSQL_CODE} model class, generate the proper Mermaid code for the diagram type.

Generate a Mermaid sequence diagram with the following specifications:

1. **Participants and Actors**:
   - Define participants using `participant` followed by the name.
   - Use the `actor` keyword for actor symbols.
   - Aliases can be defined with `participant Alias as Name` or `actor Alias as Name`.

2. **Messages**:
   - Use these arrows for messages between participants:
     - `->` for solid lines without arrowheads.
     - `-->` for dotted lines without arrowheads.
     - `->>` for solid lines with arrowheads.
     - `-->>` for dotted lines with arrowheads.
     - `<<->>` for solid bidirectional arrowheads.
     - `<<-->>` for dotted bidirectional arrowheads.
     - `-x` for solid lines with a cross (indicating destruction).
     - `--x` for dotted lines with a cross.
     - `-)` for solid lines with an open arrow (async message).
     - `--)` for dotted lines with an open arrow (async message).

3. **Loops and Conditional Statements**:
   - Use `loop` followed by a description to indicate a loop.
   - Use `alt` for alternative paths with `else` for different conditions.
   - Use `opt` for optional sequences.

4. **Grouping**:
   - Use `box` followed by a color or description to group participants or actions.
   - Close the group with `end`.

5. **Notes**:
   - Add notes using `Note [right of | left of | over] [Participant]: Note text`.
   - For multi-participant notes, use `Note over Participant1, Participant2: Note text`.

6. **Parallel and Critical Sections**:
   - Use `par` for parallel actions, with `and` separating each sequence.
   - Use `critical` for critical actions, with `option` for different conditions.

7. **Customization**:
   - Use aliases or line breaks in actor names where necessary (e.g., `participant A as "Alice<br>Johnson"`).
   - Escape characters using HTML entity codes (e.g., `#9829;` for ♥).

8. **Additional Features**:
   - Enable `autonumber` for automatic numbering of messages.
   - Include actor menus with `link Actor: Label @ URL`.

Ensure the Mermaid code is valid and adheres to these guidelines. Avoid unsupported symbols or characters not specified here. 

**Instruction to generate the proper Mermaid code for the sequence diagram**:
- Do not include any description, and do not include the backticks.
- Correct any syntax errors in the generated Mermaid code.
- Avoid any block stops or commas.
- Do not include the angle brackets or tags like `<`, `>`, `>>`, `<<`, `List<String>`, `Optional<String>`, `ResponseEntity<String>`, `ResponseEntity<?>`.
- Do not include activation and deactivation commands in the Mermaid code.

- You are an expert in generating Mermaid diagrams. Based on the following PL/SQL code, create a Mermaid {UML_DIAGRAM} diagram.
- Provide the complete Mermaid code for this {UML_DIAGRAM} diagram.
- Output only the Mermaid code. Do not include any additional text or explanations.
- Ensure that the Mermaid code is valid and can be rendered correctly.

 """



 
sequence_diagram1="""

Create a Mermaid diagram of type {UML_DIAGRAM} for the provided data. Your task is to generate the Mermaid code block that represents the sequence diagram.
For the given {PLSQL_CODE} model class generate the proper Marmaid code for the diagram_type.
 
Generate a Mermaid sequence diagram with the following specifications:
 
1. **Participants and Actors**:
   - Define participants using `participant` followed by the name.
   - If you need to use an actor symbol instead of a rectangle, use the `actor` keyword.
   - Aliases can be used by specifying `participant Alias as Name` or `actor Alias as Name`.
 
2. **Messages**:
   - Use the following types of arrows for messages between participants:
     - `->` for a solid line without an arrowhead.
     - `-->` for a dotted line without an arrowhead.
     - `->>` for a solid line with an arrowhead.
     - `-->>` for a dotted line with an arrowhead.
     - `<<->>` for a solid line with bidirectional arrowheads.
     - `<<-->>` for a dotted line with bidirectional arrowheads.
     - `-x` for a solid line with a cross at the end (indicating destruction).
     - `--x` for a dotted line with a cross at the end.
     - `-)` for a solid line with an open arrow at the end (async message).
     - `--)` for a dotted line with an open arrow at the end (async message).
 
3. **Activation and Deactivation**:
   - Use `activate` and `deactivate` to control the lifeline activation of participants.
   - Alternatively, append `+` and `-` to the message arrow to activate or deactivate participants.
 
4. **Loops and Conditional Statements**:
   - Use `loop` followed by a description to indicate a loop in the sequence.
   - Use `alt` for alternative paths with `else` for different conditions.
   - Use `opt` for optional sequences.
 
5. **Grouping**:
   - Use `box` followed by a color or description to group participants or actions.
   - Close the group with `end`.
 
6. **Notes**:
   - Add notes using `Note [right of | left of | over] [Participant]: Note text`.
   - For multi-participant notes, use `Note over Participant1, Participant2: Note text`.
 
7. **Parallel and Critical Sections**:
   - Use `par` to show parallel actions, with `and` separating each parallel sequence.
   - Use `critical` to indicate critical actions, with `option` for different conditions.
 
8. **Breaks and Background Highlights**:
   - Use `break` to indicate a stop in the sequence (e.g., for exceptions).
   - Use `rect rgb(r, g, b)` or `rect rgba(r, g, b, a)` to highlight parts of the sequence.
 
9. **Customization**:
   - Use aliases or line breaks in actor names where necessary (e.g., `participant A as "Alice<br>Johnson"`).
   - Ensure proper escaping of characters using HTML entity codes (e.g., `#9829;` for ♥).
 
10. **Additional Features**:
    - Enable `autonumber` for automatic numbering of messages.
    - Include actor menus with `link Actor: Label @ URL`.
   
 
Ensure the Mermaid code is valid and adheres to these guidelines. Avoid using any unsupported symbols or characters not specified here.
 
Strictly follow the specification symbols and Provide the Mermaid code as the output.
 
 
   Instruction must need to follow to generate the proper mermaid code class diagram:
      - Do not include any description, do not include the \`\`\`.
      - Correct generated mermaid code if any syntax error present.
      - Do not include any BLOCK STOPS, Do not include any COMMAS
      - except the sequence diagram in mermaid code strictly dont include >>, <<, >, <. if tag will be there it wont generate the diagrams.
      - dont include the Angle brackets,tags like <, >, >>, << List<String>, Optional<String>, ResponseEntity<String>, << >>, ResponseEntity<String>, ResponseEntity<?>. please dont include any open tag or close tag, Greater than sign or Less than sign.
      - dont include activate and deactivate in the mermaid code.
           
      Example format for mermaid class diagram:
      ```mermaid
      sequenceDiagram
         Alice->>+John: Hello John, how are you?
         Alice->>+John: John, can you hear me?
         John-->>-Alice: Hi Alice, I can hear you!
         John-->>-Alice: I feel great!
      ```  
 
      use the above one as example create proper class diagram.
"""  
 
 
 
 
 
 
ER_Diagram= """
         - You are an expert in generating Mermaid diagrams. Based on the following PL/SQL code, create a Mermaid {UML_DIAGRAM} diagram.
         - Provide the complete Mermaid code for this {UML_DIAGRAM} diagram.
         - Output only the Mermaid code. Do not include any additional text or explanations.
         - Ensure that the Mermaid code is valid and can be rendered correctly.
            Create a Mermaid diagram of type {UML_DIAGRAM} for the provided data. Your task is to generate the Mermaid code block that represents the described diagram.
            For the given {PLSQL_CODE} model class generate the proper Marmaid code for the diagram_type.
 
            Generate a Mermaid ER diagram with the following specifications:
 
         1. **Entities and Attributes**:
            - Define entities using the syntax: `ENTITY attributeType attributeName `.
            - Use singular nouns for entity names.
            - You may include attributes within each entity. Attributes can be marked with:
            - `PK` for Primary Key
            - `FK` for Foreign Key
            - `UK` for Unique Key
            - Optionally, add comments using double quotes after the attribute, e.g., `int age "Age in years"`.
            - Data types can include `string`, `int`, `float`, `string[]`, or custom types like `string(99)`.
 
         2. **Relationships**:
            - Define relationships using crow's foot notation with the following symbols:
             - for a one-to-one relationship.
            -  for a one-to-many relationship.
             - for a many-to-many relationship.
             - for a non-identifying relationship (dashed line).
            - Label relationships using `: "relationship label"`, or leave the label as an empty string (`: ""`).
            - Relationships may be identifying (solid line) or non-identifying (dashed line), depending on whether the child entity can exist independently.
 
         3. **Cardinality**:
            - Use the following cardinality symbols:
            - `||` for exactly one.
            - `|o` for zero or one.
            -      for one or more.
            -      for zero or more.
 
         4. **Entity Aliases**:
            - Add aliases to entities using square brackets, e.g., `ENTITY[Alias]`.
            - Display the alias in the diagram instead of the entity name.
 
         5. **Relationship Syntax**:
            - Write relationships using the format: `ENTITY1 [relationship] ENTITY2 : "relationship label"`.
            - If the relationship label has multiple words or requires line breaks, use double quotes and `<br />` for line breaks.
 
         6. **Styling**:
            - Optionally, style entities and attributes using `fill` for background color and `stroke` for border color. Example: `fill: #f9f, stroke: #333`.
            - Apply different styling to even and odd rows using `er.attributeBoxEven` and `er.attributeBoxOdd`.
 
         7. **Advanced Features**:
            - Use multi-line labels for relationships with `<br />` in the label text, e.g., `"first line<br />second line"`.
            - Include optional foreign keys in attributes if needed for clarity, or omit them for abstract models.
 
         Ensure the Mermaid code is valid and adheres to these guidelines. Avoid using unsupported characters or symbols. Provide the Mermaid code as the output.
 
 
            Instruction must need to follow or else diagram cant able to generate:
            -Do not include any description, do not include the \`\`\`.
            -Correct generated mermaid code if any syntax error present.
            -Do not include any BLOCK STOPS. Do not include any COMMAS
            -Strictly generate mermaid code for entire input.
            -Please make sure, only the Mermaid code block is required without any additional descriptions or code block delimiters.
           
            Specific insructions for generating the ER diagram:
            - Do not include any numbers inside the brackets like Decimal(10,2).
            - a line may contains only one FK or PK. Not more than one like int room_id PK FK, int amenity_id PK FK. If more than one FR and PK in a line it wont generate the diagram.
            - If word could be 'cart item','belongs to' means dont give space in-between need to mention as 'cartItem', 'belongsto'
            - except the sequence diagram in mermaid code strictly dont include >>, <<, >, <. if tag will be there it wont generate the diagrams.
            - strictly Dont include back ticks ``` and mermain in the output.
            - Field must contains single colon only more then will remove it.
            - In flowchart TD Dont include '()' this kind of brackets. If include in code it wont generete diagramtic output.
"""
 
 
 
 

 
State_Diagram= """
         - You are an expert in generating Mermaid diagrams. Based on the following PL/SQL code, create a Mermaid {UML_DIAGRAM} diagram.
         - Provide the complete Mermaid code for this {UML_DIAGRAM} diagram.
         - Output only the Mermaid code. Do not include any additional text or explanations.
         - Ensure that the Mermaid code is valid and can be rendered correctly.
            Create a Mermaid diagram of type {UML_DIAGRAM} for the provided data. Your task is to generate the Mermaid code block that represents the described diagram.
            For the given {PLSQL_CODE} model class generate the proper Marmaid code for the diagram_type.
 
         Generate a Mermaid state diagram with the following specifications:
 
1. **State Definition**:
   - Use `[stateId]` for simple states.
   - Optionally, define states using the `state` keyword or `stateId: "State description"`.
   - Avoid using any unsupported characters or symbols in state names. Use only alphanumeric characters, underscores, or dashes.
 
2. **Transitions**:
   - Use only the following symbols for transitions between states:
     - `-->` for regular transitions between states.
     - `[start state] --> [end state]` to indicate the flow of transitions.
     - Add optional labels on transitions using `: "label"`, e.g., `s1 --> s2: "A transition"`.
     - Avoid using other symbols for transitions.
 
3. **Start and End States**:
   - Represent start and end states using the special syntax `[*]` for both start and stop points in the diagram.
 
4. **Composite States**:
   - Use the `state` keyword followed by the state name and braces Curly bracket to represent composite states.
   - Composite states can contain internal states, transitions, and nested composite states.
   - Transitions between composite states should follow the same `-->` syntax.
 
5. **Choices and Forks**:
   - Use `<<choice>>` for decision points in the diagram.
   - Use `<<fork>>` for forks and `<<join>>` for joins, ensuring transitions to multiple states are clearly shown.
 
6. **Concurrency**:
   - Use `--` (double dashes) to indicate concurrency in state diagrams.
 
7. **Notes**:
   - Add notes to the right or left of a state using the syntax `note right of [stateId]: "Note text"`, or `note left of [stateId]: "Note text"`.
   - Avoid unsupported symbols within notes.
 
8. **Styling**:
   - Apply styles using the `classDef` keyword to define custom styles. Use these CSS-like properties: `fill`, `color`, `stroke-width`, `font-style`, etc.
   - Apply classes to states with the `class [stateName] [className]` syntax or the `:::operator` shorthand.
 
9. **Direction**:
   - Optionally set the direction of the diagram using `direction LR` (Left-to-Right) or `direction TB` (Top-to-Bottom).
 
10. **Comments**:
    
 
Ensure the Mermaid code is valid and adheres to these specifications. Avoid using any unsupported characters or symbols for transitions, states, or relationships. Provide the Mermaid code as the output.
 
         Ensure the Mermaid code is valid and adheres to these guidelines. Avoid using unsupported characters or symbols. Provide the Mermaid code as the output.
 
 
            Common Instruction must need to follow or else diagram cant able to generate:
            -Do not include any description, do not include the \`\`\`.
            -Correct generated mermaid code if any syntax error present.
            -Do not include any BLOCK STOPS. Do not include any COMMAS
            -Strictly generate mermaid code for entire input.
            -Please make sure, only the Mermaid code block is required without any additional descriptions or code block delimiters.
           
            Specific insructions for generating the state diagram:
            - If word could be 'cart item','belongs to' means dont give space in-between need to mention as 'cartItem', 'belongsto'
            - except the sequence diagram in mermaid code strictly dont include >>, <<, >, <. if tag will be there it wont generate the diagrams.
            - strictly Dont include back ticks ``` and mermain in the output.
            - Field must contains single colon only more then will remove it.
            - In flowchart TD Dont include '()' this kind of brackets. If include in code it wont generete diagramtic output.
 
            """
 
 
 
 
 
 
 
 
 

 
 
Mindmap="""
 
Create a Mermaid diagram of type {UML_DIAGRAM} for the provided data. Your task is to generate the Mermaid code block that represents the described diagram.
For the given {PLSQL_CODE} model class generate the proper Marmaid code for the diagram_type.
 
Generate a Mermaid mindmap diagram with the following specifications:
 
1. **Root Node**:
   - Begin with a single root node using the syntax: `RootNode`.
   - Ensure no special characters or unsupported symbols are used in the root name. Stick to alphanumeric characters, underscores, or dashes.
 
2. **Hierarchy and Levels**:
   - Structure the mindmap using indentation to indicate hierarchy. Child nodes are indented under their parent nodes.
   - Follow this structure:
     - Root level node: `RootNode`.
     - First-level nodes: Indented by one level.
     - Second-level nodes: Indented by two levels, and so on.
   - Ensure that the indentation is consistent, as inconsistent indentation may affect the diagram’s rendering.
 
3. **Node Shapes**:
   - Use the following shapes for nodes:
     - `[ ]` for squares.
     - `( )` for rounded squares.
     - `(( ))` for circles.
     - `)) ((` for "bang" shapes.
     - `)` for clouds.
     
   - Avoid using other special characters or symbols not listed here for defining shapes.
 
4. **Icons** (optional):
   - Add icons to nodes using the `::icon()` syntax, e.g., `::icon(fa fa-book)` for FontAwesome icons.
   - Ensure the icon classes follow this format without using unsupported symbols.
 
6. **Node Classes** (optional):
   - Apply CSS-like styling classes to nodes using the `:::className` syntax, e.g., `NodeA:::urgent`.
   - The available classes must be predefined (e.g., `urgent`, `large`), and custom styles should follow valid CSS properties like `fill`, `color`, or `font-weight`.
 
7. **Example Layout**:
   - Ensure the layout looks like a traditional mindmap, where:
     - Major branches come out of the root.
     - Sub-branches extend from each major branch.
     - Each node represents a major idea or concept.
 
Provide the Mermaid code as the output, ensuring all node shapes, hierarchies, and relationships are properly formatted.
 
 
   Ensure the Mermaid code is valid and adheres to these specifications. Avoid using any unsupported characters or symbols for transitions, states, or relationships. Provide the Mermaid code as the output.
 
         Ensure the Mermaid code is valid and adheres to these guidelines. Avoid using unsupported characters or symbols. Provide the Mermaid code as the output.
 
 
            Common Instruction must need to follow or else diagram cant able to generate:
            -Do not include any description, do not include the \`\`\`.
            -Correct generated mermaid code if any syntax error present.
            -Do not include any BLOCK STOPS. Do not include any COMMAS
            -Strictly generate mermaid code for entire input.
            -Please make sure, only the Mermaid code block is required without any additional descriptions or code block delimiters.
           
            Specific insructions for generating the state diagram:
            - If word could be 'cart item','belongs to' means dont give space in-between need to mention as 'cartItem', 'belongsto'
            - except the sequence diagram in mermaid code strictly dont include >>, <<, >, <. if tag will be there it wont generate the diagrams.
            - strictly Dont include back ticks ``` and mermain in the output.
            - Field must contains single colon only more then will remove it.
- You are an expert in generating Mermaid diagrams. Based on the following PL/SQL code, create a Mermaid {UML_DIAGRAM} diagram.
- Provide the complete Mermaid code for this {UML_DIAGRAM} diagram.
- Output only the Mermaid code. Do not include any additional text or explanations.
- Ensure that the Mermaid code is valid and can be rendered correctly.
"""
 
Flowchart="""
Create a Mermaid diagram of type {UML_DIAGRAM} for the provided data. Your task is to generate the Mermaid code block that represents the described diagram.
For the given {PLSQL_CODE} model class generate the proper Marmaid code for the diagram_type.
- You are recognized as an expert in generating Mermaid diagrams. Based on the PL/SQL code provided, your task is to create a Mermaid {UML_DIAGRAM} diagram that fully represents the structure and relationships as specified above.
- Please provide the complete Mermaid code for this {UML_DIAGRAM} diagram. 
- Ensure that the output consists solely of the Mermaid code; do not include any additional text, comments, or explanations in the output.
- Verify that the generated Mermaid code is valid and can be rendered accurately without any errors.


 
Create a Mermaid flowchart using the following syntax and guidelines:
 
1. Begin with:
   flowchart TD
 
2. Define nodes and connections:
   A[Node text] --> B[Node text]
   A --> C[Node text]
   B --> D/Decision/
   C --> D
   D -->|Yes| E[Result]
   D -->|No| F[Result]
 
3. Node shapes:
   [] for rectangle nodes
   () for round-edged nodes
   clery bracket for diamond (decision) nodes
   (()) for circle nodes
   [() for stadium-shaped nodes
   [()] for cylindrical nodes
   
4. Connections:
   --> for normal arrows
   --- for lines without arrows
   -.-> for dotted line arrows
   ==> for thick arrows
 
5. Labels on connections:
   -->|Label text| or --> |Label text|
 
6. Subgraphs:
   subgraph Title
     node1 --> node2
   end
 
7. Styling:
   style A fill:#f9f,stroke:#333,stroke-width:4px
   classDef className fill:#f96,stroke:#333,stroke-width:4px
   class A,B className
 
8. Comments:
   %/% This is a comment
 
9. Use descriptive one-letter IDs for nodes (A, B, C, etc.)
 
10. Avoid special characters in node text
 
11. For longer node text, use line breaks with <br>
 
12. Orient graph TD (top-down) or LR (left-right)
 
13. Use meaningful node text and connection labels
 
14. Limit diagram complexity for readability
 
Generate a flowchart depicting [describe your desired process or system].
 
 
 
Instruction must need to follow or else diagram cant able to generate:
-Do not include any description, do not include the \`\`\`.
-Correct generated mermaid code if any syntax error present.
-Do not include any BLOCK STOPS
-Do not include any COMMAS
-Strictly generate mermaid code for entire input.
-Please make sure, only the Mermaid code block is required without any additional descriptions or code block delimiters.
 
- If word could be 'cart item','belongs to' means dont give space in-between need to mention as 'cartItem', 'belongsto'
- except the sequence diagram in mermaid code strictly dont include >>, <<, >, <. if tag will be there it wont generate the diagrams.
- strictly Dont include back ticks ``` and mermain in the output.
- Field must contains single colon only more then will remove it.
- If class diagram contains empty class means Strictly dont add in the mermind generating code. like class ProductNotFoundException  class ProductRepository  class SpringBootApplications
- dont include the Angle brackets,tags like <, >, >>, << List<Product>, Optional<Product>, ResponseEntity<Product>, <<SpringBootApplication>>, ResponseEntity<String>, ResponseEntity<?>. please dont include any open tag or close tag, Greater than sign or Less than sign  
- In flowchart TD Dont include '()' this kind of brackets. If include in code it wont generete diagramtic output.

"""
 
 
 