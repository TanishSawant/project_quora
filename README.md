# Gurukul

User friendly quiz web-app, where students can login to their accounts to attempt practice tests and various multiple choice questions of physics, chemistry and mathematics.

## General concepts and motivation:

> College project is the main motivation XD

Students opting for CET exam find it difficult to get dataset of questions for practice. Also, it becomes very difficult to revise all the questions solved.

#### The challenge:
- It was difficult to figure out and finalize the framework having the most efficacy. Also, it was difficult to choose a good database system for this kind of project.
- It was indubitable that the models needed for storing questions were going to be different than the ones needed for storing user credentials.

## Commendabe features
> There are many features that can be updated in much more efficient way.

- Student can solve a random question.
- Number of tests are available for free.
- Student can choose the test he/she wants to attempt.
- There is a feature using which, user can track his/her progress and revise the questions he/she solved earlier.

## Frameworks used
-  [`Django`](https://www.djangoproject.com/) (Python framework used for routing and building views)
-  [`Jinja template engine`](https://jinja.palletsprojects.com/en/2.11.x/) (Modifying html code)
-  [`Firebase`](https://firebase.google.com/) (Database)

## Back End
- #### Models:
	- `User Model:` Django inbuilt User. 
	
  <br/>
  
	- `Question Model:`

  <br/>

```python
	class Question(models.Model):
	    statement = models.TextField(unique = True)
	    optionA = models.TextField()
	    optionB = models.TextField()
	    optionC = models.TextField()
	    optionD = models.TextField()
	    CorrectOption = models.CharField(max_length = 2)
	    questionId = models.TextField(unique = True)
	    subject = models.CharField(max_length = 50, null = False)
	    test = models.ForeignKey(Test, unique = False, on_delete = models.CASCADE)

```
    
    
| Field      |    Type | 
| :-------- | --------:| 
| Statement   |   TextField | 
| Option A   |   TextField |
| Option B  |   TextField |
| Option C   |   TextField |			
| Option D   |   TextField |
| Correct Option   |   CharField |
| Question ID  |   TextField |
| Subject   |   TextField |
| Test   |   Foreign Key(Test) |


  - Test:

<br/>

```python
	class Test(models.Model):
	    user = models.ForeignKey(User, unique = False, on_delete = models.CASCADE)
	    testId = models.TextField(unique = True)
	    description = models.TextField(default="Default Description")
```


| Field      | Type | 
| :-------- | --------:| 
| user    |   Foreign Key(User) | 
| Test ID   |   Text Field |
| Description    |   Text Field |

## Sequence Diagram:




## Screenshots

![Home Page](./1608448733244.png)

![Dashboard 1](./1608448779982.png)

![Dashboard 2](./1608448816718.png)

![list of tests](./1608448843506.png)

![Alt text](./1608448857263.png)

![Revision](./1608448908734.png)

