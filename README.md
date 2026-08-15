# WorkNest – Django Multi-Tier DevOps Application

WorkNest is a production-oriented task management web application built with Django and PostgreSQL and containerized using Docker.

The project is designed as a foundation for implementing a complete DevOps workflow using GitHub, Jenkins, Docker, Kubernetes, AWS, Prometheus, and Grafana.

---

## 📌 Project Overview

WorkNest is a multi-tier web application that allows users to:

- Register and log in
- Create tasks
- View tasks
- Update tasks
- Delete tasks
- Manage tasks associated with authenticated users
- Store application data in PostgreSQL

The application follows a layered architecture with Django as the web application layer and PostgreSQL as the database layer.

The project is containerized using Docker Compose and is designed to be extended into a complete AWS DevOps deployment.

---

## 🏗️ Current Architecture

```text
                    User
                     │
                     │ HTTP :8000
                     ▼
             ┌─────────────────┐
             │    WorkNest     │
             │     Django      │
             │    Gunicorn     │
             │    Container    │
             └────────┬────────┘
                      │
                      │ PostgreSQL
                      │ db:5432
                      ▼
             ┌─────────────────┐
             │   PostgreSQL    │
             │      18         │
             │    Container    │
             └─────────────────┘


🚀 Features
------> User registration                         <------ 
------> User authentication                       <------
------> Login/logout functionality                <------
------> Protected task management                 <------
------> Create tasks                              <------
------> Update tasks                              <------
------> Delete tasks                              <------
------> User-specific task management             <------
------> PostgreSQL database integration           <------
------> Django ORM                                <------
------> Database migrations                       <------
------> Automated tests                           <------
------> Responsive web interface                  <------
------> Docker containerization                   <------
------> Docker Compose multi-container setup      <------
------> Gunicorn production WSGI server           <------
------> Health check for PostgreSQL               <------
------> Environment-based configuration           <------


🛠️ Technology Stack
------------> Application Technologies

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| Python     | Application programming language   |
| Django     | Web application framework          |
| Django ORM | Database abstraction and queries   |
| PostgreSQL | Relational database                |
| HTML5      | Web page structure                 |
| CSS3       | User interface styling             |
| Gunicorn   | Production WSGI application server |

------------> DevOps Technologies

| Technology     | Purpose                                  |
| -------------- | ---------------------------------------- |
| Git            | Version control                          |
| GitHub         | Source code management and collaboration |
| Docker         | Application containerization             |
| Docker Compose | Running Django and PostgreSQL together   |
| Jenkins        | CI/CD automation                         |
| Kubernetes     | Container orchestration and deployment   |
| AWS EC2        | Cloud compute environment                |
| Prometheus     | Application and infrastructure metrics   |
| Grafana        | Monitoring dashboards and visualization  |


🔧 Technology Usage

| Technology     | Where It Is Used       | Purpose                              |
| -------------- | ---------------------- | ------------------------------------ |
| Python         | Application            | Backend programming                  |
| Django         | Web container          | Web framework                        |
| PostgreSQL     | Database container     | Persistent application data          |
| Gunicorn       | Web container          | Production application server        |
| Docker         | Application deployment | Creates reproducible containers      |
| Docker Compose | Local development      | Runs multi-container application     |
| Git            | Development            | Version control                      |
| GitHub         | Repository             | Source code hosting                  |
| Jenkins        | CI/CD                  | Automates build, test and deployment |
| AWS EC2        | Cloud                  | Hosts DevOps infrastructure          |
| Kubernetes     | AWS/EC2 environment    | Container orchestration              |
| Prometheus     | Monitoring environment | Collects metrics                     |
| Grafana        | Monitoring environment | Displays monitoring dashboards       |

worknest-django-devops/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── webapp/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   ├── templates/
│   │   └── webapp/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── task_list.html
│   │       ├── task_form.html
│   │       └── task_confirm_delete.html
│   │
│   ├── static/
│   │   └── webapp/
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── README.md

🏛️ Application Architecture

WorkNest follows a multi-tier architecture.

| Layer               | Technology                  | Responsibility                      |
| ------------------- | --------------------------- | ----------------------------------- |
| Presentation Layer  | HTML, CSS, Django Templates | User interface                      |
| Application Layer   | Django                      | Business logic and request handling |
| Data Access Layer   | Django ORM                  | Database communication              |
| Database Layer      | PostgreSQL                  | Persistent data storage             |
| Application Server  | Gunicorn                    | Serves Django application           |
| Container Layer     | Docker                      | Application isolation               |
| Orchestration Layer | Kubernetes                  | Container deployment and scaling    |
| Monitoring Layer    | Prometheus + Grafana        | Metrics and visualization           |


📌 Project Status

------------ Status: Completed ------------ 

------------  implementation  ------------

✅ Django application
✅ PostgreSQL
✅ Authentication
✅ Task management
✅ CSS UI
✅ Automated tests
✅ Docker
✅ Docker Compose
✅ Gunicorn
✅ PostgreSQL persistent volume
✅ AWS deployment
✅ Jenkins CI/CD 
✅ Kubernetes 
✅ Prometheus/Grafana 

👨‍💻 Author

HariHaran A

AWS DevOps Engineer | Cloud & DevOps

GitHub:
https://github.com/Hariharan14-Dev
