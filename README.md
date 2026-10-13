# TRACE — A Social Network for the Journey, Not Just the Destination

**TRACE** is a journey-based social network where people document their progress toward personal and professional goals. Instead of sharing only achievements, users can share milestones, setbacks, lessons learned, and the process behind their growth.

The project is being developed backend-first using **FastAPI**, with the goal of learning backend engineering fundamentals, understanding the framework through its official documentation, and building a production-quality portfolio project.

> **Core idea:** Social media for the work in progress.

---

## Table of Contents

* [1. Project Overview](#1-project-overview)
* [2. Problem Statement](#2-problem-statement)
* [3. Product Vision](#3-product-vision)
* [4. Core Features](#4-core-features)
* [5. MVP Scope](#5-mvp-scope)
* [6. Technology Stack](#6-technology-stack)
* [7. Architecture](#7-architecture)
* [8. Project Structure](#8-project-structure)
* [9. Database Design](#9-database-design)
* [10. API Design](#10-api-design)
* [11. Privacy and Authorization](#11-privacy-and-authorization)
* [12. Development Roadmap](#12-development-roadmap)
* [13. Testing Strategy](#13-testing-strategy)
* [14. Security Considerations](#14-security-considerations)
* [15. Future Improvements](#15-future-improvements)
* [16. Learning Resources](#16-learning-resources)
* [17. Development Principles](#17-development-principles)
* [18. Project Status](#18-project-status)

---

## 1. Project Overview

TRACE allows users to create journeys around goals they want to achieve and document their progress over time.

Examples of journeys include:

* Becoming a software engineer.
* Learning a new programming language.
* Building and launching a startup.
* Learning a musical instrument.
* Completing a personal challenge.
* Developing a new professional skill.

Each journey contains a goal, description, timeline, milestones, and progress updates.

Other users can follow journeys, leave comments, offer encouragement, and learn from the experiences of others.

### What makes TRACE different?

Traditional social media often focuses on individual posts and finished achievements. TRACE organizes content around an ongoing journey.

Its defining features are:

1. **Journey-based following:** Follow a specific journey rather than only following a person's profile.
2. **Progress documentation:** Record achievements, setbacks, and lessons learned.
3. **Milestone tracking:** Break larger goals into smaller checkpoints.
4. **Long-term context:** Keep updates connected in a chronological journey timeline.
5. **Retrospectives:** Summarize what worked, what failed, and what was learned when a journey ends.

The aim is to make the process of growth as valuable to share as the final result.

---

## 2. Problem Statement

Many people pursue long-term goals without a structured way to document their progress or connect with others working toward similar goals.

Existing social platforms make it easy to share individual posts, but a user's journey can become fragmented across many unrelated updates.

TRACE explores a different approach: making the journey itself the central unit of social interaction.

Users should be able to document their work, receive meaningful feedback, and build a lasting record of their progress.

---

## 3. Product Vision

TRACE should become a community where people can:

* Start documenting a goal before they have achieved it.
* Break a large goal into manageable milestones.
* Share progress honestly, including setbacks.
* Learn from the experiences of other people.
* Follow journeys that interest them.
* Reflect on their progress and capture lessons learned.

### Example user journey

A developer creates a journey titled:

**"Become confident building production-ready APIs in 90 days."**

They create milestones for learning FastAPI, designing a relational database, implementing authentication, writing tests, and deploying an application.

Throughout the journey, they publish updates about what they have learned, what they have struggled with, and what they plan to do next.

Other users follow the journey, comment on updates, and share useful suggestions.

At the end, the developer publishes a retrospective documenting their progress and lessons learned.

---

## 4. Core Features

### 4.1 User Accounts

Users can register, authenticate, and manage their profiles.

Each user has a unique identity and can create multiple journeys.

### 4.2 Journeys

A journey represents a goal that a user wants to pursue.

Each journey contains:

* A title.
* A description.
* A creator.
* A start date.
* An optional target date.
* A lifecycle status.
* A visibility setting.
* A collection of milestones.
* A collection of progress updates.

Users can create, retrieve, update, and delete their own journeys.

### 4.3 Milestones

Milestones represent checkpoints within a journey.

A journey can contain multiple milestones, each with its own title, description, position, status, and optional due date.

For the MVP, milestones can be marked as pending or completed.

### 4.4 Progress Updates

Users document what happens during a journey through progress updates.

Initial update types:

* `progress`: Something the user accomplished.
* `setback`: A challenge or difficulty encountered.
* `lesson`: Something the user learned.

Each update belongs to a journey and has a creation timestamp.

### 4.5 Comments

Users can comment on progress updates to ask questions, provide suggestions, and encourage other users.

Comments are associated with their authors and the updates they belong to.

### 4.6 Journey Following

Users can follow individual journeys.

This is distinct from following a person's entire profile. A user may be interested in someone's programming journey without needing to follow every journey that person creates.

### 4.7 Feed

The feed displays progress updates from journeys a user follows.

The initial implementation will use a straightforward chronological feed, with pagination.

### 4.8 Retrospectives

A completed journey can eventually have a retrospective that summarizes the experience.

This feature will be implemented after the core MVP is functional.

---

## 5. MVP Scope

The MVP will focus on delivering a working social experience with a reliable backend.

### Included in the MVP

* User registration and login.
* User profiles.
* Journey CRUD.
* Private-by-default journey visibility.
* Milestone creation and status updates.
* Progress updates.
* Comments on progress updates.
* Following and unfollowing journeys.
* A paginated chronological feed.
* Input validation and consistent error handling.
* Database persistence.
* Automated tests.
* API documentation.
* Deployment-ready configuration.

### Excluded from the initial MVP

The following features will be considered later:

* Direct messaging.
* Real-time chat.
* Video uploads.
* AI-generated recommendations.
* Complex feed-ranking algorithms.
* Collaborative journeys.
* Advanced analytics.
* Mobile applications.
* Microservices.
* Redis-based caching before a demonstrated need.

The priority is to implement the essential features correctly before expanding the product.

---

## 6. Technology Stack

### Backend

* **Python:** Primary programming language.
* **FastAPI:** HTTP API framework.
* **Pydantic:** Request validation and response schemas.
* **SQLAlchemy 2.x:** Object-relational mapping and database access.
* **Alembic:** Database migrations.
* **PostgreSQL:** Relational database.
* **pytest:** Automated testing.
* **HTTPX / FastAPI TestClient:** HTTP endpoint testing.

### Authentication and security

* Secure password hashing using an established password-hashing library.
* Bearer-token authentication.
* JWT access tokens if JWT is selected for the authentication implementation.
* Authorization checks for resource ownership and visibility.
* Environment-based configuration for secrets and database credentials.

### Development and deployment

* Git and GitHub for version control.
* Docker for containerization.
* A managed PostgreSQL database for deployment.
* Environment variables for configuration.

### Future frontend

The frontend will be built after the backend MVP is functional.

Planned technologies:

* React or Next.js.
* TypeScript.
* A suitable styling system.
* The TRACE REST API.

The frontend framework and detailed UI design can be finalized later.

---

## 7. Architecture

TRACE will use a **modular monolith with a layered architecture**.

This is inspired by MVC but adapted for a JSON API consumed by a separate frontend.

### Architectural layers

#### API / Router Layer

Responsibilities:

* Define HTTP endpoints.
* Receive and validate requests.
* Declare response models and status codes.
* Use FastAPI dependencies.
* Call the appropriate service.
* Return HTTP responses.

Business rules and complex database queries should not accumulate in route handlers.

#### Schema Layer

Pydantic schemas define the data accepted and returned by the API.

For example:

* `JourneyCreate`: fields accepted when creating a journey.
* `JourneyUpdate`: fields that may be updated.
* `JourneyResponse`: fields returned to clients.

Input schemas and output schemas should be separate where their responsibilities differ.

#### Service Layer

The service layer implements application workflows and business rules.

Examples:

* Creating a journey with private visibility by default.
* Checking whether a status transition is allowed.
* Ensuring a user is authorized to modify a journey.
* Coordinating updates involving multiple related records.

#### Repository Layer

The repository layer contains database-access operations.

Examples:

* Retrieving a journey by ID.
* Listing journeys belonging to a user.
* Creating and retrieving progress updates.
* Loading comments for an update.

A repository layer is an architectural choice, not a requirement imposed by FastAPI. It will be used in TRACE to practice separation of concerns and make data access easier to test.

#### Model Layer

SQLAlchemy models represent database tables, columns, relationships, constraints, and indexes.

They are distinct from Pydantic request and response schemas.

#### Database Layer

This layer manages database configuration, the SQLAlchemy engine, session creation, and model metadata.

Database sessions will be provided through FastAPI dependencies.

### Request lifecycle

A typical request follows this flow:

1. The client sends an HTTP request.
2. The router validates the request using Pydantic.
3. FastAPI dependencies provide required resources and authentication information.
4. The service applies business rules.
5. The repository accesses the database.
6. The service returns the result.
7. The router returns a response matching the declared response schema.

---

## 8. Project Structure

The following structure is the intended target. Files will be introduced incrementally as the project grows.

```text
trace/
├── app/
│   ├── main.py
│   ├── dependencies.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── session.py
│   │   └── base.py
│   ├── models/
│   │   ├── user.py
│   │   ├── journey.py
│   │   ├── milestone.py
│   │   ├── progress_update.py
│   │   ├── comment.py
│   │   └── journey_follow.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── journey.py
│   │   ├── milestone.py
│   │   ├── progress_update.py
│   │   ├── comment.py
│   │   └── journey_follow.py
│   ├── api/
│   │   └── routes/
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── journeys.py
│   │       ├── milestones.py
│   │       ├── updates.py
│   │       ├── comments.py
│   │       ├── follows.py
│   │       └── feed.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── journey_service.py
│   │   ├── milestone_service.py
│   │   └── progress_service.py
│   └── repositories/
│       ├── user_repository.py
│       ├── journey_repository.py
│       ├── milestone_repository.py
│       ├── progress_repository.py
│       └── comment_repository.py
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_journeys.py
│   ├── test_milestones.py
│   ├── test_updates.py
│   ├── test_comments.py
│   ├── test_follows.py
│   └── test_feed.py
├── alembic/
├── .env.example
├── .gitignore
├── pyproject.toml
├── alembic.ini
├── Dockerfile
└── README.md
```

The structure is not a requirement to create every file immediately. Start small and introduce modules when their responsibilities become necessary.

---

## 9. Database Design

PostgreSQL will store the application's persistent data.

The initial relational model consists of the following entities.

### 9.1 User

Represents a registered account.

| Field           | Purpose                      |
| --------------- | ---------------------------- |
| `id`            | Primary key                  |
| `username`      | Unique public username       |
| `email`         | Unique email address         |
| `password_hash` | Secure password hash         |
| `bio`           | Optional profile description |
| `created_at`    | Account creation timestamp   |

### 9.2 Journey

Represents a goal created by a user.

| Field         | Purpose                     |
| ------------- | --------------------------- |
| `id`          | Primary key                 |
| `user_id`     | Foreign key to the creator  |
| `title`       | Journey title               |
| `description` | Goal description            |
| `start_date`  | Journey start date          |
| `due_date`    | Optional target date        |
| `status`      | Journey lifecycle status    |
| `visibility`  | Access level                |
| `created_at`  | Creation timestamp          |
| `updated_at`  | Last modification timestamp |

Initial journey statuses:

* `active`
* `paused`
* `completed`
* `abandoned`

Initial visibility values:

* `private`
* `public`

The visibility default is **private**. A journey must not become public unless the creator explicitly chooses public visibility.

### 9.3 Milestone

Represents a checkpoint within a journey.

| Field          | Purpose                            |
| -------------- | ---------------------------------- |
| `id`           | Primary key                        |
| `journey_id`   | Foreign key to its journey         |
| `title`        | Milestone title                    |
| `description`  | Optional description               |
| `position`     | Order within the journey           |
| `status`       | Completion status                  |
| `due_date`     | Optional deadline                  |
| `completed_at` | Completion timestamp, if completed |
| `created_at`   | Creation timestamp                 |

Initial milestone statuses:

* `pending`
* `completed`

### 9.4 ProgressUpdate

Represents a progress entry within a journey.

| Field         | Purpose                      |
| ------------- | ---------------------------- |
| `id`          | Primary key                  |
| `journey_id`  | Foreign key to its journey   |
| `author_id`   | Foreign key to its author    |
| `content`     | Update content               |
| `update_type` | Progress, setback, or lesson |
| `created_at`  | Publication timestamp        |
| `updated_at`  | Last modification timestamp  |

Initial update types:

* `progress`
* `setback`
* `lesson`

### 9.5 Comment

Represents a comment on a progress update.

| Field        | Purpose                            |
| ------------ | ---------------------------------- |
| `id`         | Primary key                        |
| `update_id`  | Foreign key to the progress update |
| `author_id`  | Foreign key to the commenter       |
| `content`    | Comment text                       |
| `created_at` | Creation timestamp                 |
| `updated_at` | Last modification timestamp        |

### 9.6 JourneyFollow

Represents a user's subscription to a journey.

| Field        | Purpose                             |
| ------------ | ----------------------------------- |
| `id`         | Primary key                         |
| `user_id`    | Foreign key to the follower         |
| `journey_id` | Foreign key to the followed journey |
| `created_at` | Follow timestamp                    |

A unique database constraint on `(user_id, journey_id)` will prevent duplicate follows.

### Relationships

* One user can create many journeys.
* One journey can contain many milestones.
* One journey can contain many progress updates.
* One progress update can have many comments.
* One user can comment on many progress updates.
* Users can follow many journeys.
* One journey can have many followers.

### Data integrity rules

* Foreign keys enforce valid relationships.
* Unique constraints protect usernames, emails, and follow relationships.
* Status and visibility values must be validated.
* Required fields cannot be empty.
* Database transactions should protect operations that change multiple related records.
* Deletion behavior must be explicitly chosen for related records.

Journey progress can initially be calculated from completed milestones rather than stored as an independently editable percentage. If a percentage is shown, the UI must clearly define what it means.

---

## 10. API Design

The API will use REST conventions and JSON request and response bodies.

The following endpoints describe the planned MVP. Exact request and response schemas will be defined during implementation.

### 10.1 Authentication

| Method  | Endpoint         | Purpose                                   |
| ------- | ---------------- | ----------------------------------------- |
| `POST`  | `/auth/register` | Register a user                           |
| `POST`  | `/auth/token`    | Authenticate and obtain an access token   |
| `GET`   | `/users/me`      | Retrieve the authenticated user's profile |
| `PATCH` | `/users/me`      | Update the authenticated user's profile   |

### 10.2 Journeys

| Method   | Endpoint                 | Purpose                                |
| -------- | ------------------------ | -------------------------------------- |
| `POST`   | `/journeys/`             | Create a journey                       |
| `GET`    | `/journeys/`             | List journeys visible to the requester |
| `GET`    | `/journeys/{journey_id}` | Retrieve a single accessible journey   |
| `PATCH`  | `/journeys/{journey_id}` | Update an owned journey                |
| `DELETE` | `/journeys/{journey_id}` | Delete an owned journey                |
| `GET`    | `/users/me/journeys`     | List the authenticated user's journeys |

### 10.3 Milestones

| Method   | Endpoint                            | Purpose                          |
| -------- | ----------------------------------- | -------------------------------- |
| `POST`   | `/journeys/{journey_id}/milestones` | Create a milestone               |
| `GET`    | `/journeys/{journey_id}/milestones` | List journey milestones          |
| `GET`    | `/milestones/{milestone_id}`        | Retrieve an accessible milestone |
| `PATCH`  | `/milestones/{milestone_id}`        | Update a milestone               |
| `DELETE` | `/milestones/{milestone_id}`        | Delete a milestone               |

### 10.4 Progress Updates

| Method   | Endpoint                         | Purpose                       |
| -------- | -------------------------------- | ----------------------------- |
| `POST`   | `/journeys/{journey_id}/updates` | Publish a progress update     |
| `GET`    | `/journeys/{journey_id}/updates` | List updates for a journey    |
| `GET`    | `/updates/{update_id}`           | Retrieve an accessible update |
| `PATCH`  | `/updates/{update_id}`           | Edit an owned update          |
| `DELETE` | `/updates/{update_id}`           | Delete an owned update        |

### 10.5 Comments

| Method   | Endpoint                        | Purpose                 |
| -------- | ------------------------------- | ----------------------- |
| `POST`   | `/updates/{update_id}/comments` | Comment on an update    |
| `GET`    | `/updates/{update_id}/comments` | List comments           |
| `PATCH`  | `/comments/{comment_id}`        | Edit an owned comment   |
| `DELETE` | `/comments/{comment_id}`        | Delete an owned comment |

### 10.6 Journey Following

| Method   | Endpoint                        | Purpose                |
| -------- | ------------------------------- | ---------------------- |
| `PUT`    | `/journeys/{journey_id}/follow` | Follow a journey       |
| `DELETE` | `/journeys/{journey_id}/follow` | Unfollow a journey     |
| `GET`    | `/users/me/following`           | List followed journeys |

The follow operation should be idempotent: repeating the request must not create duplicate relationships.

### 10.7 Feed

| Method | Endpoint | Purpose                                 |
| ------ | -------- | --------------------------------------- |
| `GET`  | `/feed`  | Retrieve updates from followed journeys |

The feed will initially be chronological and paginated.

### HTTP behavior

The API should use appropriate HTTP status codes, including:

* `200 OK` for successful retrieval or updates.
* `201 Created` for successful resource creation.
* `204 No Content` for successful deletion where no body is returned.
* `401 Unauthorized` when authentication is missing or invalid.
* `403 Forbidden` when access is explicitly denied.
* `404 Not Found` when a resource cannot be found or is intentionally concealed.
* `409 Conflict` for conflicts such as duplicate unique values.
* `422 Unprocessable Entity` for request validation failures.

The exact response for inaccessible resources should be chosen consistently to avoid leaking private resource information.

---

## 11. Privacy and Authorization

Privacy is a core product requirement, not a feature to add at the end.

### Default visibility

Every new journey will have `visibility = private` unless the creator explicitly requests public visibility.

A missing visibility field must not cause a journey to become public.

### Private journeys

Only the journey owner can access a private journey in the initial MVP.

The owner can manage its milestones and progress updates.

Private journey data must not leak through:

* Public journey listings.
* Search results.
* Feeds.
* Milestone endpoints.
* Progress-update endpoints.
* Comments or related-resource endpoints.

### Public journeys

Public journeys may be viewed by other users, subject to the API's authentication and product policies.

Only the owner can edit or delete the journey and manage its milestones.

### General authorization rules

* Users cannot edit another user's profile.
* Users cannot edit or delete another user's journey.
* Users cannot publish updates to journeys they do not own.
* Users cannot edit or delete another user's comments.
* Users cannot follow a private journey they cannot access.
* Every endpoint that accepts a resource ID must verify the relevant permissions.

Authorization must be enforced on the backend, regardless of what the frontend displays.

---

## 12. Development Roadmap

Development will proceed incrementally, with each phase producing a working and testable result.

### Phase 1: Understand FastAPI and build the first API

**Goal:** Implement journey CRUD while learning the framework.

Tasks:

* Set up the Python project.
* Create the FastAPI application.
* Define Pydantic request and response schemas.
* Implement journey creation and retrieval.
* Add journey updates and deletion.
* Validate request data.
* Use correct HTTP status codes.
* Explore the automatically generated `/docs` interface.
* Write initial endpoint tests.

Temporary in-memory storage may be used for the first learning exercise, but it will be replaced with a persistent database.

**Completion criteria:** Journey CRUD works, input validation behaves correctly, and the implementation can be explained without relying on a tutorial.

### Phase 2: Database and persistence

**Goal:** Understand relational data modeling and database integration.

Tasks:

* Set up PostgreSQL.
* Learn SQLAlchemy models and sessions.
* Define database relationships.
* Implement the database session dependency.
* Replace in-memory storage.
* Add Alembic migrations.
* Add constraints and indexes where appropriate.
* Test database operations.

**Completion criteria:** Data persists across restarts, relationships work correctly, and database changes are versioned through migrations.

### Phase 3: Authentication and authorization

**Goal:** Protect user data.

Tasks:

* Implement registration.
* Hash passwords securely.
* Implement login and token authentication.
* Create a dependency for the current authenticated user.
* Protect private endpoints.
* Enforce resource ownership.
* Implement private-by-default journey visibility.
* Test unauthorized and forbidden access.

**Completion criteria:** Users can access their own protected resources without being able to modify other users' data.

### Phase 4: Milestones and progress updates

**Goal:** Implement the core TRACE experience.

Tasks:

* Create and manage milestones.
* Create and manage progress updates.
* Validate journey and milestone states.
* Add update types.
* Implement pagination.
* Apply privacy checks to related resources.

**Completion criteria:** Users can document a journey from its creation through its progress, with consistent data and authorization rules.

### Phase 5: Comments and journey following

**Goal:** Add social interactions.

Tasks:

* Implement comments.
* Implement follow and unfollow operations.
* Enforce uniqueness for follow relationships.
* Handle duplicate requests safely.
* Add pagination and sorting.
* Test cross-user access.

**Completion criteria:** Users can interact with accessible journeys without violating privacy or ownership rules.

### Phase 6: Feed and query efficiency

**Goal:** Provide a useful social feed.

Tasks:

* Build a chronological feed.
* Return updates from followed journeys.
* Exclude inaccessible private content.
* Implement pagination.
* Inspect SQL queries.
* Add indexes where justified.
* Test empty feeds and large result sets.

**Completion criteria:** The feed returns the right updates in the right order without exposing private data or loading every record at once.

### Phase 7: Production readiness

**Goal:** Make the backend reliable and deployable.

Tasks:

* Expand automated tests.
* Add consistent error handling.
* Configure structured logging.
* Manage secrets through environment variables.
* Validate configuration at startup.
* Add Docker support.
* Document setup and migrations.
* Deploy the API and database.
* Verify the deployment.

**Completion criteria:** Another developer can set up the project from the README, run the tests, and use the deployed API.

### Phase 8: Frontend development

**Goal:** Build the user interface after the backend API is stable.

Potential screens:

* Registration and login.
* User profile.
* Journey discovery.
* Journey creation and editing.
* Journey detail and timeline.
* Milestone management.
* Progress-update creation.
* Comments.
* Followed-journey feed.
* Account and privacy settings.

The frontend will consume the existing REST API rather than duplicate backend business rules.

---

## 13. Testing Strategy

Testing is part of development, not an activity reserved for the end.

### Unit tests

Test business rules independently where practical.

Examples:

* Journey status transitions.
* Default visibility.
* Milestone completion behavior.
* Validation of update types.

### API integration tests

Test endpoints through FastAPI's testing utilities.

Examples:

* Creating a journey.
* Retrieving a journey.
* Updating an owned journey.
* Rejecting unauthorized edits.
* Listing milestones.
* Publishing progress updates.
* Adding comments.
* Following a journey.
* Retrieving the feed.

### Database tests

Test relationships, constraints, transactions, and persistence using a controlled test database.

### Security tests

Verify that:

* Invalid credentials are rejected.
* Protected endpoints require authentication.
* Users cannot access private journeys they do not own.
* Users cannot modify another user's resources.
* Private content does not leak through nested or list endpoints.
* Invalid input is handled correctly.

### Edge cases

Include tests for:

* Missing resources.
* Empty strings and invalid field values.
* Duplicate usernames and emails.
* Duplicate follow operations.
* Invalid status transitions.
* Missing or expired tokens.
* Empty result sets.
* Pagination boundaries.

---

## 14. Security Considerations

Security decisions will be made as the relevant features are implemented.

* Store password hashes, never plaintext passwords.
* Use an established password-hashing implementation.
* Keep secrets out of source control.
* Validate input using Pydantic and database constraints.
* Enforce authorization on every protected resource.
* Use transactions when multiple database changes must succeed or fail together.
* Avoid exposing stack traces or internal exception details to clients.
* Apply rate limiting to sensitive endpoints when appropriate.
* Use HTTPS in production.
* Configure CORS for the actual frontend origin rather than allowing every origin by default.
* Choose token expiration and revocation behavior deliberately.
* Prevent private data from leaking through list endpoints, feeds, and related resources.

---

## 15. Future Improvements

Once the MVP works reliably, TRACE can be extended with:

* Journey retrospectives.
* Likes or reactions on progress updates.
* Notifications.
* Background task processing.
* Image attachments.
* Search and discovery filters.
* User profile following.
* Journey collaboration.
* WebSockets for real-time notifications.
* Feed optimization.
* Caching where measurements justify it.
* Observability and performance testing.

Each feature should be introduced to solve a defined product or engineering problem, not merely to increase the number of technologies in the stack.

---

## 16. Learning Resources

The official documentation will be the primary learning resource.

### FastAPI

* [First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
* [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
* [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
* [Request Body](https://fastapi.tiangolo.com/tutorial/body/)
* [Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
* [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
* [Bigger Applications — Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
* [SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
* [Security](https://fastapi.tiangolo.com/tutorial/security/)
* [Testing](https://fastapi.tiangolo.com/tutorial/testing/)
* [Settings](https://fastapi.tiangolo.com/advanced/settings/)
* [Deployment Concepts](https://fastapi.tiangolo.com/deployment/concepts/)

### Supporting documentation

* [SQLAlchemy 2.x documentation](https://docs.sqlalchemy.org/en/20/)
* [Alembic documentation](https://alembic.sqlalchemy.org/en/latest/)
* [Pydantic documentation](https://docs.pydantic.dev/latest/)
* [PostgreSQL documentation](https://www.postgresql.org/docs/)
* [pytest documentation](https://docs.pytest.org/en/stable/)

### Learning method

For each feature:

1. Identify the concept you need to learn.
2. Read the relevant official documentation.
3. Implement the feature independently.
4. Write tests.
5. Explain why the implementation works.
6. Review edge cases and security implications.
7. Refactor only when you understand the problem the refactoring solves.

The objective is not simply to finish the application. It is to understand the engineering decisions behind it.

---

## 17. Development Principles

TRACE will follow these principles throughout development:

1. **Documentation first:** Use official documentation to learn concepts rather than copying end-to-end tutorials.
2. **Incremental development:** Build one small, working feature at a time.
3. **Separation of concerns:** Keep API handling, validation, business rules, and data access distinct.
4. **Security by design:** Make privacy and authorization part of the initial architecture.
5. **Test important behavior:** Cover both successful requests and failure cases.
6. **Keep complexity justified:** Avoid premature microservices, caching, and infrastructure.
7. **Document decisions:** Record important architectural choices and their trade-offs.
8. **Understand the code:** Be able to explain every major component in a technical interview.
9. **Measure before optimizing:** Use query inspection and performance measurements to guide improvements.
10. **Build for maintainability:** Prefer understandable, consistent code over unnecessary abstraction.


**TRACE — The journey matters as much as the destination.**
