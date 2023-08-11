# Part 1 - Analytical Dashboard
The goal of the Analytical Dashboard is to provide a convenient way for users to make racing analysis with different perspective in one dashboard. 
<br><br>
This is a prototype of the Analytical Dashboard of the F1 Analysis project.

## Setup
Build the dashboard application by docker build and docker run with the following code:

```
docker build -t f1_analysis_prototype .
docker run -h localhost -p 9002:8000 -d --name f1_dashboard f1_analysis_prototype
```

## Prototype Gallery
<img src=prototype_dashboard.png>

## Future Plan
Coming soon...