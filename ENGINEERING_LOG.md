# StudentOS Engineering Log

StudentOS is a personal productivity and academic management system built with Flask.

This document records the engineering progress of the project, including completed work, architectural decisions, implementation notes, resolved issues, and upcoming milestones.

---

## Sessions

| Session | Topic | Status |
|---------:|------------------------------------|:------:|
| 1 | Project Setup | ✅ |
| 2 | First Flask Application | ✅ |
| 3 | Templates & UI Foundation | ✅ |
| 4 | Multi-page Navigation | ✅ |
| 5 | Dashboard Layout | ✅ |
| 6 | Professional Dashboard UI | ✅ |
| 7 | Reusable Dashboard Components | ✅ |
| 8 | Dynamic Data with Flask & Jinja | ✅ |

---

# Session 1 - Project Setup

**Date:** 2026-07-27

## Goal

Establish a clean development environment and create the initial structure for the StudentOS project.

---

## Completed

- Created the StudentOS project directory.
- Initialized a Git repository.
- Created and activated a Python virtual environment.
- Installed Flask.
- Generated `requirements.txt`.
- Added `.gitignore` for Python projects.
- Organized the initial project structure.

---

## Engineering Decisions

- Used a virtual environment to isolate project dependencies.
- Chose Git from the beginning to maintain version history.
- Stored project dependencies inside `requirements.txt` for reproducible environments.
- Kept the initial project structure minimal to allow gradual expansion.

---

## Issues & Fixes

- None.

---

## Git

- Initial project setup.
- Repository initialized.

---

## Next

- Build the first Flask application.
- Configure the application entry point.
- Verify the development server.

---

# Session 2 - First Flask Application

**Date:** 2026-07-27

## Goal

Create the first working Flask application and verify the development workflow.

---

## Completed

- Implemented the Flask Application Factory pattern.
- Created `run.py` as the application entry point.
- Added the home route (`/`).
- Successfully launched the development server.
- Connected the project to GitHub.
- Configured SSH authentication.
- Pushed the repository to GitHub.

---

## Engineering Decisions

- Adopted the Application Factory pattern to keep the project scalable.
- Separated the application entry point from the application package.
- Used SSH authentication for GitHub to simplify future development.

---

## Issues & Fixes

- Configured SSH keys to resolve GitHub authentication.

---

## Git

- Added the first working Flask application.
- Connected the local repository to GitHub.

---

## Next

- Introduce Jinja templates.
- Integrate Bootstrap.
- Build a reusable page layout.

---

# Session 3 - Templates & UI Foundation

**Date:** 2026-07-27

## Goal

Create a reusable user interface that can serve as the foundation for the entire StudentOS application.

---

## Completed

- Added Jinja2 template inheritance.
- Created `base.html`.
- Created the landing page (`index.html`).
- Integrated Bootstrap 5.
- Added custom CSS.
- Created reusable navigation and footer components.
- Established the project's template structure.

---

## Engineering Decisions

- Used template inheritance to eliminate repeated HTML across pages.
- Centralized shared UI components inside reusable templates.
- Added Bootstrap through the base template so every page shares the same design system.
- Stored custom styling inside `style.css` to separate presentation from templates.

---

## Issues & Fixes

- Resolved `TemplateAssertionError`.
- Fixed `TemplateNotFound` while organizing reusable templates.

---

## Git

- Added reusable template structure.
- Integrated Bootstrap and custom styling.

---

## Next

- Expand StudentOS into a multi-page application.
- Build dashboard navigation.
- Replace hardcoded links with Flask routing.

# Session 4 - Multi-page Navigation

**Date:** 2026-07-27

## Goal

Transform StudentOS from a single-page Flask application into a structured multi-page web application.

---

## Completed

- Created the Dashboard page.
- Created the Academics page.
- Created the Cyber Hub page.
- Added Flask routes for each page.
- Expanded the navigation bar to support multiple pages.
- Replaced hardcoded links with `url_for()`.

---

## Engineering Decisions

- Assigned a dedicated route and template to each module to improve project organization.
- Used `url_for()` instead of hardcoded URLs to make navigation independent of future route changes.
- Established a modular page structure that can easily accommodate new features.

---

## Issues & Fixes

- None.

---

## Git

- Added multi-page navigation.
- Connected all pages through Flask routing.

---

## Next

- Design the StudentOS dashboard.
- Create summary cards for important academic information.
- Build a responsive dashboard layout.

---

# Session 5 - Dashboard Layout

**Date:** 2026-07-27

## Goal

Design the first version of the StudentOS dashboard and establish a consistent layout for future modules.

---

## Completed

- Created the dashboard page layout.
- Added four summary cards:
  - Subjects
  - Study Hours
  - Tasks
  - CGPA
- Implemented a responsive Bootstrap Grid layout.
- Verified responsive behavior across different screen sizes.

---

## Engineering Decisions

- Selected Bootstrap Cards to present dashboard statistics in a clean and modular format.
- Used the Bootstrap Grid System to ensure responsive layouts without custom positioning.
- Designed the dashboard to allow additional widgets without major structural changes.

---

## Issues & Fixes

- None.

---

## Git

- Added the initial dashboard layout.
- Implemented responsive dashboard cards.

---

## Next

- Improve the dashboard UI.
- Add icons and visual hierarchy.
- Enhance the user experience with animations.

---

# Session 6 - Professional Dashboard UI

**Date:** 2026-07-28

## Goal

Improve the dashboard interface by introducing better visual hierarchy, reusable styling, and interactive elements.

---

## Completed

- Integrated Bootstrap Icons.
- Redesigned all dashboard summary cards.
- Added meaningful icons for each dashboard metric.
- Applied contextual color styling.
- Introduced a welcome banner.
- Improved typography using Bootstrap utility classes.
- Added hover animations using custom CSS.
- Verified responsiveness after the redesign.

---

## Engineering Decisions

- Used Bootstrap Icons instead of image assets to maintain scalability and reduce project size.
- Applied Bootstrap utility classes before writing custom CSS to minimize unnecessary styling.
- Stored custom styles inside `style.css` to keep templates clean.
- Added hover effects to improve user interaction while preserving a lightweight interface.

---

## Issues & Fixes

- None.

---

## Git

- Redesigned the dashboard interface.
- Added icons, animations, and responsive UI improvements.

---

## Next

- Refactor duplicated dashboard components.
- Introduce reusable Jinja2 macros.
- Improve maintainability by applying the DRY principle.

# Session 7 - Reusable Dashboard Components

**Date:** 2026-07-28

## Goal

Reduce duplicated dashboard code by introducing reusable Jinja2 components and improve the maintainability of the template structure.

---

## Completed

- Created a reusable dashboard card macro.
- Imported the macro into the dashboard template.
- Replaced duplicated dashboard card HTML with macro calls.
- Verified that the dashboard appearance remained unchanged after refactoring.

---

## Engineering Decisions

- Used a Jinja2 macro instead of `{% include %}` because each dashboard card requires different data.
- Moved repeated HTML into a single reusable component to simplify future modifications.
- Refactored the dashboard without changing its visual appearance or functionality.
- Separated page structure from reusable UI components to improve maintainability.

---

## Issues & Fixes

- Initially considered using `{% include %}` for dashboard cards.
- Replaced the approach with a Jinja2 macro after identifying that parameterized components were a better fit.

---

## Git

- Refactored dashboard cards using reusable Jinja2 macros.

---

## Next

- Replace hardcoded dashboard values with dynamic data.
- Pass variables from Flask routes into templates.
- Introduce Jinja template logic.

---

# Session 8 - Dynamic Data with Flask & Jinja

**Date:** 2026-07-28

## Goal

Transform the dashboard from a static interface into a dynamic page by passing data from Flask to Jinja templates.

---

## Completed

- Moved dashboard values from the template into the Flask route.
- Passed variables to templates using `render_template()`.
- Replaced hardcoded values with Jinja variables.
- Added conditional rendering using Jinja `if` statements.
- Generated the study task list dynamically using a Jinja `for` loop.
- Verified that dashboard content updates automatically when Python data changes.

---

## Engineering Decisions

- Kept application data inside Flask routes while leaving templates responsible only for presentation.
- Used Jinja variables instead of hardcoded values to prepare the project for future database integration.
- Implemented conditional rendering to allow the interface to respond to application state.
- Generated repeated HTML using loops instead of manually duplicating markup.
- Followed a clear data flow:

  Python → Flask Route → Jinja Template → Browser

---

## Issues & Fixes

- The CGPA value was initially displayed as the literal text `"cgpa"` because quotation marks were used around the variable.
- Removed the quotation marks so Jinja evaluated the variable correctly.

---

## Git

- Added dynamic template rendering.
- Introduced Jinja variables, conditionals, and loops.

---

## Next

- Integrate SQLite.
- Configure SQLAlchemy.
- Replace temporary Python variables with persistent database records.

---

# Roadmap

## Core Platform

- Flask
- SQLite
- SQLAlchemy
- Application Configuration

---

## Academic Module

- Subject Manager
- Semester Manager
- CGPA Tracker
- Study Session Logger

---

## Productivity Module

- Task Manager
- Pomodoro Timer
- Habit Tracker

---

## Knowledge Module

- Flashcards
- PDF Organizer
- Notes Manager

---

## Analytics

- Dashboard Charts
- Weekly Reports
- Study Statistics

---

## UI & UX

- Dark Mode
- Responsive Improvements
- Accessibility Enhancements

---

## Deployment

- Production Configuration
- Docker Support
- Cloud Deployment
- Custom Domain

# Session 9 - Database Foundation (SQLite & SQLAlchemy)

**Date:** 2026-07-28

## Goal

Transform StudentOS from a static Flask application into a database-backed application by introducing SQLite and SQLAlchemy. Improve the project architecture to support future growth while maintaining clean separation of responsibilities.

---

## Completed

### Project Architecture

- Refactored application routes into a dedicated `routes` package.
- Introduced Flask Blueprints.
- Simplified `create_app()` by separating routing from application initialization.
- Updated all template navigation to use Blueprint endpoints.

### Configuration

- Created `config.py` for centralized application configuration.
- Added application configuration using the `Config` class.
- Configured SQLite as the project's database.
- Disabled SQLAlchemy modification tracking.

### Database

- Installed Flask-SQLAlchemy.
- Configured SQLAlchemy using the Application Factory pattern.
- Created a shared SQLAlchemy instance.
- Initialized SQLAlchemy with the Flask application.
- Created the project's first database model (`Task`).
- Registered the models package.
- Generated the first SQLite database (`studentos.db`).
- Created the initial database table using `db.create_all()`.

### Project Structure

Current project structure:

```text
StudentOS/
│
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── static/
│   └── templates/
│
├── config.py
├── ENGINEERING_LOG.md
├── README.md
├── requirements.txt
├── run.py
└── studentos.db
```

---

## Engineering Decisions

### Blueprint Architecture

Adopted Flask Blueprints to separate application routing from application initialization. This keeps `create_app()` focused on application setup while allowing the project to scale by organizing routes into independent modules.

### Centralized Configuration

Moved application settings into `config.py` instead of scattering configuration values throughout the project. This makes future development environments (development, testing, production) easier to manage.

### Database Selection

Selected SQLite as the initial database because it is lightweight, serverless, and well suited for personal projects and learning. The architecture allows migration to PostgreSQL or another relational database in the future with minimal code changes.

### ORM Selection

Used SQLAlchemy instead of raw SQL to interact with the database using Python classes. This improves readability, maintainability, and database portability.

### First Model Selection

Started with the `Task` model because it is independent and does not require relationships with other tables. This allows database fundamentals to be learned before introducing more advanced concepts such as foreign keys and relationships.

### Application Factory Compatibility

Initialized SQLAlchemy using `db.init_app(app)` instead of `SQLAlchemy(app)` to maintain compatibility with the Application Factory pattern adopted in earlier sessions.

---

## Issues & Fixes

### Blueprint Endpoint Error

**Issue**

After introducing Flask Blueprints, template navigation stopped working.

**Cause**

Blueprints automatically prefix endpoint names.

Example:

```python
url_for("home")
```

became

```python
url_for("main.home")
```

**Resolution**

Updated all `url_for()` calls to use Blueprint-prefixed endpoint names.

---

### IndentationError

**Issue**

Python raised an `IndentationError` after introducing:

```python
with app.app_context():
```

**Cause**

The body of the `with` block was not properly indented.

**Resolution**

Indented `db.create_all()` correctly inside the application context.

---

### Circular Import

**Issue**

Python raised:

```text
ImportError: cannot import name 'db'
```

**Cause**

The models package was imported before the SQLAlchemy instance had been initialized, resulting in a circular import.

**Resolution**

Delayed importing the models package until after SQLAlchemy had been initialized inside `create_app()`.

---

## Git

### Added

- Flask Blueprints
- Centralized configuration
- SQLAlchemy integration
- SQLite database
- Task model
- Models package
- Database initialization

### Refactored

- Moved routes into the `routes` package.
- Simplified `create_app()`.
- Updated template navigation to use Blueprint endpoints.

---

## Next

- Understand CRUD operations.
- Insert the first Task into the database.
- Retrieve Task records using SQLAlchemy queries.
- Update existing records.
- Delete records.
- Replace temporary dashboard task data with database-backed data.
- Introduce Flask-Migrate to replace `db.create_all()` with proper database migrations in a future session.

# Session 10 - CRUD (Create & Read)

**Date:** 2026-07-29

## Goal

Implement the first CRUD operations by allowing users to create study tasks through a web form and display database-backed tasks on the dashboard.

---

## Completed

### Database

- Queried all tasks using `Task.query.all()`.
- Counted tasks using `Task.query.count()`.
- Replaced hardcoded dashboard task data with SQLite records.

### Forms

- Created `add_task.html`.
- Built the first HTML form.
- Used the POST method for data submission.
- Retrieved form data using `request.form`.

### Routes

- Added `/add-task` supporting both GET and POST requests.
- Redirected users to the dashboard after successfully creating a task.

### Dashboard

- Displayed database-backed tasks.
- Added an "Add Task" button.
- Displayed task titles using Jinja object attributes.

---

## Engineering Decisions

- Used POST instead of GET for creating records.
- Redirected after successful submission to prevent accidental duplicate form submissions.
- Kept the temporary `/create-task` route only for learning purposes and planned its removal after completing form-based task creation.

---

## Issues & Fixes

### Task Object Display

**Issue**

Dashboard displayed:

```
<Task Complete Algorithms Assignment>
```

instead of only the task title.

**Cause**

The template rendered the entire Task object.

**Resolution**

Updated the template to use:

```jinja
{{ task.title }}
```

instead of:

```jinja
{{ task }}
```

### Task Counter

Improved task counting by replacing:

```python
len(study_tasks)
```

with:

```python
Task.query.count()
```

---

## Git

### Added

- Add Task page
- HTML form
- POST request handling
- Dashboard integration
- Database-backed task list

### Improved

- Efficient task counting
- Dashboard navigation

---

## Next

- Understand database primary keys.
- Update existing tasks.
- Delete tasks.
- Add task completion status.
- Introduce Flask-Migrate for production-style database management.

# Session 11

## Goal
Implement the remaining CRUD operations (Update and Delete) for study tasks and connect them to the dashboard.

---

## Completed

- Added Edit and Delete buttons to each task.
- Implemented Delete functionality using a dynamic Flask route.
- Connected Delete button with `url_for()`.
- Learned how dynamic routes work using `<int:id>`.
- Used `Task.query.get_or_404()` to safely retrieve tasks.
- Deleted tasks using:
  - `db.session.delete()`
  - `db.session.commit()`
- Implemented Edit functionality using GET and POST methods.
- Created `edit_task.html`.
- Pre-filled the edit form using:
  `value="{{ task.title }}"`
- Updated tasks without calling `db.session.add()`.
- Successfully completed all CRUD operations:
  - Create
  - Read
  - Update
  - Delete

---

## Engineering Decisions

- Used dynamic routes for task-specific actions.
- Used `get_or_404()` instead of `get()` for safer database queries.
- Allowed SQLAlchemy to automatically detect modified objects instead of re-adding them to the session.
- Kept IDs visible temporarily for learning database concepts.

---

## Issues & Fixes

### Observation
After deleting a task, the ID numbers did not decrease.

### Explanation
SQLite does not renumber primary keys after deletion. IDs are permanent identifiers, ensuring data integrity and maintaining relationships between tables.

---

## Git

Session 11 committed and pushed successfully.

---

## Next

Session 12:
- Remove temporary learning routes.
- Remove visible database IDs.
- Improve task UI.
- Add delete confirmation.
- Prepare StudentOS for Version 0.1.

# Session 12

## Goal
Clean up the task management system, improve the dashboard UI, and prepare StudentOS for Version 0.1.

---

## Completed

- Removed the temporary `/create-task` route.
- Removed visible database IDs from the dashboard.
- Added a task counter heading.
- Added an empty-state message when no tasks exist.
- Added a delete confirmation dialog using JavaScript `confirm()`.
- Implemented task completion and undo functionality.
- Added dynamic Complete/Undo button.
- Displayed completed tasks using strike-through styling.
- Improved the overall dashboard layout and user experience.

---

## Engineering Decisions

- Removed temporary learning code after it served its purpose.
- Kept primary keys internal instead of displaying them.
- Reused the existing `completed` Boolean field instead of introducing another status field.
- Used a toggle route with:
  `task.completed = not task.completed`
- Improved UX with confirmation dialogs and informative empty states.

---

## Issues & Fixes

### Improvement
The dashboard originally contained duplicated task display logic.

### Fix
Refactored the template so that the task list and empty-state message are handled in a single `{% if study_tasks %}` block.

---

## Git

Session 12 committed and pushed successfully.

---

## Next

Session 13:
- User Authentication
- Registration
- Login
- Logout
- Password hashing
- User-specific tasks

# Session 13 - User Authentication

## Goal
Implement a complete user authentication system using Flask-Login.

## Completed
- Installed and configured Flask-Login.
- Created the User model.
- Implemented password hashing and verification.
- Built Register, Login, and Logout functionality.
- Configured LoginManager and user_loader.
- Protected application routes using @login_required.
- Added a dynamic authentication-aware navbar.

## Engineering Decisions
- Used Flask-Login for session management.
- Stored passwords securely using Werkzeug hashing.
- Kept the home page public while protecting application features.
- Separated authentication into its own Blueprint.

## Issues & Fixes
- Fixed a circular import by using a lazy import inside user_loader.
- Protected all task-related routes after discovering they were publicly accessible.

## Git
Commit:
Session 13: Implement user authentication with Flask-Login

## Next
- Build a professional Bootstrap user dropdown.
- Create one-to-many User ↔ Task relationship.
- Make tasks user-specific.

# Session 14

## Goal
Implement secure one-to-many User–Task relationships and enforce task ownership.

## Completed
- Added User → Task one-to-many relationship.
- Added Task.user_id foreign key.
- Configured SQLAlchemy relationship and backref.
- Recreated SQLite database with updated schema.
- Linked new tasks to the logged-in user.
- Dashboard now displays only the logged-in user's tasks.
- Created reusable get_user_task() helper.
- Prevented unauthorized task edit, toggle, and delete operations.

## Engineering Decisions
- Used current_user from Flask-Login.
- Applied DRY by extracting ownership logic into a helper.
- Used HTTP 403 Forbidden for unauthorized access.

## Issues & Fixes
- Database schema mismatch after adding user_id.
- Recreated development database.
- Fixed RecursionError caused by recursive helper implementation.

## Git
- Implemented secure multi-user task ownership.

## Next
- Professional navbar dropdown
- User profile page
- Flash messages
- Settings page

# Session 15

## Goal
Improve the StudentOS user experience by polishing the interface, adding account navigation, and implementing application-wide feedback messages.

## Completed

### UI Improvements
- Improved global page background.
- Added navbar shadow and navigation hover effects.
- Improved dashboard card styling.
- Added smoother card hover effects.
- Improved buttons and task-list styling.
- Improved general visual hierarchy.

### User Navigation
- Replaced separate username and Logout links with a Bootstrap account dropdown.
- Added Profile, Settings, and Logout options.
- Created a protected Profile page.
- Created a protected Settings page.
- Connected Profile and Settings to the account dropdown.

### Flash Message System
- Added global flash-message rendering to base.html.
- Added dismissible Bootstrap alerts.
- Added feedback for:
  - Task creation
  - Empty task titles
  - Task completion
  - Task undo
  - Task editing
  - Task deletion
  - Registration
  - Login
  - Invalid login
  - Logout

### Authentication Improvements
- Added basic registration validation.
- Prevented duplicate usernames.
- Prevented duplicate email addresses.
- Normalized email input using strip() and lower().
- Replaced plain-text login errors with proper flash messages.

## Engineering Concepts Learned
- Information architecture
- Global reusable UI components
- Separation of concerns
- User feedback and flash messages
- Input normalization
- Application-level validation
- Database uniqueness constraints
- Incremental UI improvement

## Testing
Verified:
- User registration
- Duplicate username detection
- Duplicate email detection
- Successful login
- Invalid login
- Logout
- Profile authentication
- Settings authentication
- Account dropdown
- Task creation
- Empty task validation
- Task editing
- Task completion/undo
- Task deletion
- Flash-message dismissal

## Next
- Improve Profile functionality.
- Begin editable account information.
- Continue incremental StudentOS UI improvements.
- Consider improving task routes to use appropriate HTTP methods.

# Session 16

## Goal
Improve the Profile interface, correct task action HTTP methods, and implement secure profile editing.

## Completed

### UI Improvements
- Improved Profile page presentation.
- Added a dedicated profile avatar.
- Added scoped `.profile-card` styling.
- Added structured profile information panels.
- Improved visual hierarchy without affecting unrelated cards.

### HTTP Method Improvements
- Changed task Complete/Undo from GET requests to POST requests.
- Changed task Delete from GET to POST.
- Converted Complete/Undo and Delete links into HTML forms.
- Preserved Edit as a GET/POST workflow.
- Preserved delete confirmation before form submission.

### Task System Improvements
- Maintained task ownership authorization through `get_user_task()`.
- Added flash feedback for task completion.
- Added flash feedback for task undo.
- Preserved flash feedback for task creation, editing, and deletion.

### Debugging
- Encountered Flask endpoint collision:
  `AssertionError: View function mapping is overwriting an existing endpoint function: main.toggle_task`
- Identified duplicate `toggle_task()` route definitions.
- Removed the duplicate route.
- Cleaned and reorganized `main.py`.
- Restored the Edit Task route while refactoring.

### Editable Profile
- Added `/profile/edit`.
- Created `edit_profile.html`.
- Added pre-filled username and email fields.
- Added username editing.
- Added email editing.
- Normalized email input with `strip()` and `lower()`.
- Prevented empty username/email submissions.
- Prevented duplicate usernames.
- Prevented duplicate email addresses.
- Excluded the current user's own account from uniqueness checks.
- Added successful profile-update feedback.
- Updated navbar username automatically after profile changes.

## Engineering Concepts Learned
- HTTP request semantics.
- Difference between GET and POST.
- Why state-changing actions should not use GET.
- Scoped CSS.
- Route endpoint uniqueness in Flask.
- Account data validation.
- Database uniqueness checks.
- Updating authenticated user data.
- Separation between profile viewing and profile editing.

## Testing
Verified:
- Profile UI.
- Complete task.
- Undo completed task.
- Delete confirmation cancellation.
- Task deletion.
- Task editing.
- Flash messages.
- Normal profile update.
- Saving unchanged profile information.
- Duplicate username protection.
- Duplicate email protection.

All tests passed successfully.

## Security Note
Task-changing actions now use POST instead of GET.

However, POST requests are not yet protected against CSRF attacks. CSRF protection should be implemented before considering these forms production-ready.

## Next — Session 17
- Implement CSRF protection.
- Protect state-changing forms with CSRF tokens.
- Implement secure Change Password functionality.
- Verify the user's current password before allowing a password change.
- Continue incremental UI improvements.