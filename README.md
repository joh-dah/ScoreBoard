# Assignment: Build Something - Score Board

## Repository

The code can be found at https://github.com/joh-dah/ScoreBoard

## SetUp

- Start the minikube tunnel with `minikube start` and `minikube tunnel`
- Start the application with `kubectl apply -f kustomize.yaml`
- Access application via `http://10.107.57.82/`

## CleanUp
- Run `kubectl delete --cascade=foreground -f kustomize.yaml`

## Description of the Software
I built a simple scoreboard to track the scores of e.g. volleyball or table tennis matches. On the starting page, you see a list of all previous games. A new game can be created with the "New Game" button.

![Start Page](/readme_images/start_page.png)

You get redirected to a page where you can track the score of the game and afterwards return to the start page.

![Scoreboard](/readme_images/scoreboard.png)

## Software Architecture and Design

The Application consists of three microservices. The frontend, the backend and the database.

![Architecture](/readme_images/architecture.png)

### Frontend Microservice
- **Responsibility:** Provides a user interface for users to interact with the scoreboard.
- **Technology:** Vue.js
- **API:** Exposes REST endpoints to communicate with the backend.

### Backend Microservice
- **Responsibility:** Manages game entries, updates the database, and serves requested information to the frontend.
- **Technology:** Flask (Python)
- **API:** Exposes REST endpoints to communicate with the frontend. Utilizes environment variables for database connection.

### Database Microservice (MongoDB)
- **Responsibility:** Stores game data persistently.
- **Technology:** MongoDB
- **Storage:** Utilizes persistent storage for data that survives infrastructure restarts.

### Architecture Principles and Patterns
- **Microservices:** Each component (Frontend, Backend, Database) is a separate microservice, enabling independent scalability.
- **RESTful API:** Communication between microservices follows REST principles.
- **ConfigMap:** Configurations are managed using Kubernetes ConfigMap for decoupling.

### Benefits and Challenges

#### Benefits:
- **Scalability:** Microservices allow independent horizontal scaling of components.
- **Decoupling:** Components are loosely coupled, facilitating independent development and maintenance.
- **Resilience:** Persistence of MongoDB ensures data survival across infrastructure restarts.

#### Challenges:
- **Complexity:** Managing multiple microservices introduces complexity in deployment and monitoring. Espacially for a simple application like this one the three microservices are a lot of unnecessary overhead.

### Security Considerations
Ensuring secure communication between microservices is crucial. The complex architecture introduces avoidable security risks.
- **Secure Communication:** Use HTTPS and secure ports for communication between microservices.
- **Access Controls:** Implement proper access controls for database interactions.

### Mitigation Strategies

- **Automation:** Implement CI/CD pipelines for automated deployment and updates.
- **Monitoring:** Employ Kubernetes monitoring tools for tracking and analyzing microservice behavior.
- **Regular Audits:** Conduct regular security audits to identify and address vulnerabilities.
