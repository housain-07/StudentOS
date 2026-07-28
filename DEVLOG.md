# StudentOS Development Log

This document records the development progress of **StudentOS**, including features implemented, concepts learned, challenges faced, and future plans.

---

# Session 1 - Project Setup
**Date:** 2026-07-27

## Objective
Set up the development environment and initialize the StudentOS project.

## Completed
- Created the StudentOS project structure.
- Initialized a Git repository.
- Created and activated a Python virtual environment.
- Installed Flask.
- Created `requirements.txt`.
- Added `.gitignore`.

## Learned
- Why virtual environments are important.
- Basic Git workflow.
- Installing and managing project dependencies.

## Challenges
- None.

## Git
- Initial project setup committed.

## Next Session
- Create the first Flask application.

---

# Session 2 - First Flask Application
**Date:** 2026-07-27

## Objective
Build and run the first Flask application.

## Completed
- Implemented the Flask Application Factory.
- Created `run.py`.
- Added the first route (`/`).
- Successfully launched the application in the browser.

## Learned
- Flask application structure.
- Application Factory pattern.
- Basic routing.

## Challenges
- None.

## Git
- Connected the project to GitHub.
- Configured SSH authentication.
- Pushed the project to GitHub.

## Next Session
- Build the UI using templates and Bootstrap.

---

# Session 3 - Templates & UI Foundation
**Date:** 2026-07-27

## Objective
Create a reusable UI structure for StudentOS.

## Completed
- Added Jinja2 template inheritance.
- Created `base.html`.
- Created `index.html`.
- Integrated Bootstrap 5.
- Added custom CSS.
- Created reusable `navbar.html`.
- Created reusable `footer.html`.
- Built the first landing page.

## Learned
- Template inheritance.
- Static files in Flask.
- Bootstrap integration.

## Challenges
- Fixed `TemplateAssertionError`.
- Fixed `TemplateNotFound` for `footer.html`.

## Git
- Committed and pushed the UI foundation.

## Next Session
- Expand StudentOS into a multi-page application.

---

# Session 4 - Multi-page Navigation
**Date:** 2026-07-27

## Objective
Transform StudentOS from a single-page application into a multi-page Flask application.

## Completed
- Created the Dashboard page.
- Created the Academics page.
- Created the Cyber Hub page.
- Added Flask routes for each page.
- Updated the navigation bar.
- Replaced hardcoded links with `url_for()`.

## Learned
- Flask routing.
- Navigation using `url_for()`.
- Organizing multiple templates.

## Challenges
- None.

## Git
- Added multi-page navigation.

## Next Session
- Design the first dashboard.

---

# Session 5 - Dashboard Layout
**Date:** 2026-07-27

## Objective
Build the first version of the StudentOS dashboard.

## Completed
- Created a responsive dashboard layout.
- Built four Bootstrap summary cards:
  - Subjects
  - Study Hours
  - Tasks
  - CGPA
- Tested dashboard responsiveness.
- Verified navigation across all pages.

## Learned
- Bootstrap Grid System (`container`, `row`, `col`).
- Bootstrap Cards.
- Building responsive layouts.

## Challenges
- None.

## Git
- Added the first dashboard layout.

## Next Session
- Improve the dashboard design.
- Learn Bootstrap Grid in depth.
- Add icons and progress components.

---

# Session 6 - Professional Dashboard UI
**Date:** 2026-07-28

## Objective
Enhance the StudentOS dashboard with a more professional appearance by improving its layout, adding icons, and introducing interactive UI elements.

## Completed
- Added Bootstrap Icons to the project using a CDN.
- Redesigned all four dashboard summary cards.
- Added meaningful icons for:
  - Subjects
  - Study Hours
  - Tasks
  - CGPA
- Applied Bootstrap color utilities to visually distinguish each card.
- Added descriptive text beneath each dashboard statistic.
- Replaced the simple dashboard heading with a welcome banner.
- Improved typography using Bootstrap display and font utility classes.
- Added smooth hover animations to dashboard cards using custom CSS.
- Verified that the dashboard remains responsive after all UI enhancements.

## Learned
- How to integrate Bootstrap Icons into a Flask project.
- How to use Bootstrap icon classes (`bi-*`).
- Bootstrap utility classes:
  - `display-*`
  - `fs-*`
  - `fw-*`
  - `text-*`
  - `h-100`
- How Bootstrap Grid creates responsive layouts.
- How CSS `transition`, `transform`, and `box-shadow` work together to create smooth hover effects.
- Why custom styles should be placed in `style.css` instead of inline HTML.

## Challenges
- None.

## Git
- Enhanced the dashboard UI with Bootstrap Icons, improved typography, and interactive hover effects.

## Next Session
- Refactor the dashboard using reusable Jinja2 components.
- Learn the DRY (Don't Repeat Yourself) principle.
- Build reusable dashboard cards with Jinja2 `{% include %}`.

---

# Future Roadmap

## Phase 1 — Foundation ✅
- Project setup
- Flask
- GitHub
- Bootstrap
- Multi-page navigation

## Phase 2 — Dashboard 🚧
- Better UI
- Statistics
- Icons
- Progress bars

## Phase 3 — Database
- SQLite
- SQLAlchemy
- Models

## Phase 4 — Features
- Pomodoro Timer
- Task Manager
- CGPA Tracker
- Habit Tracker
- Flashcards
- PDF Organizer

## Phase 5 — Polish
- Charts
- Dark Mode
- Responsive improvements
- Deployment