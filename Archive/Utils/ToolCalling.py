Read Code
Open Program.cs

↓

Read appsettings.json

↓

Read Controllers
AI Topic

✅ Tool Calling

LLM নিজে File পড়তে পারে না।

সে বলে

read_file("Program.cs")

IDE Tool সেটা Execute করে।

এটা Function Calling-এর মতো।

LLM

↓

Function Call

↓

IDE

↓

Returns File












Install Package
dotnet add package ...
AI Topic

না।

এটা AI না।

এটা

Tool Calling

LLM শুধু Command Generate করে।

Terminal Execute করে।








Compile
dotnet build
AI Topic

Not AI.

এটা Tool।

LLM

↓

Tool Call

↓

Compiler




Run Tests
dotnet test
AI Topic

Tool Calling




. Commit
git add

git commit
AI Topic

Tool Calling