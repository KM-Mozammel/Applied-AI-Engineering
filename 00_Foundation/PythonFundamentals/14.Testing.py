"""
==================================================
01_Introduction
==================================================
Testing হলো Software-এর Code সঠিকভাবে কাজ করছে কিনা তা স্বয়ংক্রিয়ভাবে যাচাই করার প্রক্রিয়া। Professional Software Development-এ Code লেখার পাশাপাশি Test লিখাও সমান গুরুত্বপূর্ণ। Python-এ সবচেয়ে জনপ্রিয় Testing Framework হলো pytest
--------------------------------------------------
Instead of নিজে Program চালিয়ে Result দেখা Use - pytest
--------------------------------------------------
Testing-এর উদ্দেশ্য, 
✔ Bug ধরা
✔ Regression Prevent করা
✔ Refactoring Safe করা
✔ Code Quality Improve করা
✔ CI/CD Pipeline-এ Automatic Verification
--------------------------------------------------
Example,

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

==================================================
02_WhyTestingExists
==================================================
ধরো, তোমার Project-এ 500টি Function আছে। তুমি একটি Function Modify করলে। এখন কি সব ঠিক আছে? হাতে পরীক্ষা করতে গেলে অনেক সময় লাগবে। তাই Automated Test দরকার।
--------------------------------------------------
Without Testing: Code Change -> Manual Testing -> Human Error -> Production Bug
--------------------------------------------------
With Testing: Code Change -> pytest -> All Tests Passed -> Deploy
==================================================
03_Syntax
==================================================
Step 1: Install - pip install pytest
--------------------------------------------------
Step 2: Create File test_math.py
--------------------------------------------------
Example: 

def add(a, b):
    return a + b

def test_add():
    assert add(2,3)==5

--------------------------------------------------
Run pytest or pytest -v
==================================================
04_Methods
==================================================
assert: Expected Result Check করে।

Example: 
assert 5==5
assert add(2,3)==5
--------------------------------------------------
pytest.raises(): Exception Test করার জন্য।
Example:

import pytest

def divide(a,b):
    return a/b

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)

--------------------------------------------------
Fixture: Reusable Setup Code।
Example,

import pytest

@pytest.fixture
def numbers():
    return [1,2,3]

def test_sum(numbers):
    assert sum(numbers)==6

--------------------------------------------------
Multiple Fixtures: 

@pytest.fixture
def db():
    ...

@pytest.fixture
def user():

    ...

==================================================
05_TimeComplexity
==================================================
assert: O(1)
--------------------------------------------------
Fixture: Depends on Setup Cost
--------------------------------------------------
pytest: Overall Complexity Depends on Number of Tests
==================================================
06_InternalWorking
==================================================
Command: pytest
Step 1: pytest: Project Scan করে।
Step 2: সব test_* File খুঁজে।
Step 3: সব test_* Function Collect করে।
Step 4: Fixture Resolve করে।
Step 5: Test Execute করে।
Step 6: assert Evaluate করে।
Pass অথবা Fail দেখায়।
--------------------------------------------------
Flow: pytest -> Collect Tests -> Inject Fixtures -> Run Test -> assert -> Report
==================================================
07_Examples
==================================================
Example 1: Basic assert

def add(a,b):
    return a+b

def test_add():
    assert add(2,3)==5

--------------------------------------------------
Example 2: Fixture

import pytest

@pytest.fixture
def dataset():
    return [10,20,30]

def test_length(dataset):
    assert len(dataset)==3
--------------------------------------------------
Example 3: Exception Testing

import pytest

def divide(a,b):
    return a/b

def test_error():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)

--------------------------------------------------
Example 4: AI Dataset Fixture

import pytest

@pytest.fixture
def dataset():
    return [(1,3),(2,5),(3,7)]

def predict(x):
    return 2*x+1

def test_predictions(dataset):
    for x,y in dataset:
        assert predict(x)==y

--------------------------------------------------

Example 5: Model Testing

class LinearModel:
    def predict(self,x):
        return 2*x+1

def test_model():
    model=LinearModel()
    assert model.predict(5)==11

==================================================
08_CommonMistakes
==================================================
❌ Mistake 1: print() দিয়ে Test করা। print(add(2,3)) Professional নয়। ✔ assert add(2,3)==5
--------------------------------------------------
❌ Mistake 2: Fixture ব্যবহার না করা। প্রতিটি Test-এ একই Setup লেখা। ভুল। Fixture ব্যবহার করো।
--------------------------------------------------
❌ Mistake 3: সব Test এক Function-এ লেখা। ভুল, test_everything() ঠিক, test_add(), test_subtract(), test_login()
--------------------------------------------------
❌ Mistake 4: Edge Case Test না করা। শুধু Normal Input Test করলে হবে না। Zero, Negative, Empty List, None, Exception সব Test করতে হবে।

==================================================
09_Exercises
==================================================
Exercise 1: add() Function-এর Test লিখো।
--------------------------------------------------
Exercise 2: subtract() Function-এর জন্য ৩টি assert লিখো।
--------------------------------------------------
Exercise 3:  Fixture তৈরি করো। যা একটি Dataset Return করবে।
--------------------------------------------------
Exercise 4: divide() Function-এর ZeroDivisionError Test করো।
--------------------------------------------------
Exercise 5: LinearModel Class-এর predict() Method Test করো।

==================================================
10_AIUsage (Use Case in AI Development)
==================================================
AI Engineering-এ Testing অত্যন্ত গুরুত্বপূর্ণ।
--------------------------------------------------
১। Data Validation: Dataset Empty কিনা Missing Value আছে কিনা সব Test করা হয়।
--------------------------------------------------
২। Feature Engineering: Normalization, Encoding, Scaling ঠিক হয়েছে কিনা Test করা হয়।
--------------------------------------------------
৩। Model Prediction: Known Input Expected Output assert দিয়ে Verify করা হয়।
--------------------------------------------------
৪। API Testing: Prediction API ঠিক Response দিচ্ছে কিনা pytest দিয়ে Test করা হয়।
--------------------------------------------------
৫। Regression Testing: Model Update করার পর আগের Behavior পরিবর্তন হয়েছে কিনা Check করা হয়।
--------------------------------------------------
৬। CI/CD: GitHub Push, pytest, All Tests Passed, Deploy
--------------------------------------------------
৭। MLOps: Training Pipeline, Inference Pipeline , Data Pipeline সব Automated Test করা হয়।
--------------------------------------------------
Summary:  assert -> Result Verify -> pytest -> Testing Framework -> fixture -> Reusable Setup

Professional Backend, AI Engineering, Machine Learning, Data Engineering এবং Enterprise Software-এ pytest হলো Python-এর সবচেয়ে জনপ্রিয় Testing Framework।
"""