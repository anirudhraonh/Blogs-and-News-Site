# Blogs and News Site

A Django-based web application for sharing and discovering blog posts with integrated news feed functionality.

## Features

- **User Authentication**: User registration and login system with Django's built-in authentication
- **Blog Management**: Create, read, and manage blog posts with title, summary, and featured images
- **Comments System**: Users can comment on blog posts with support for images
- **News Integration**: Integrated NewsAPI for fetching latest news from multiple sources
- **Search Functionality**: Search blog posts by title using a search form
- **User Profiles**: Track blogs posted by individual users
- **Image Support**: Upload and manage featured images for blog posts with automatic cleanup on deletion
- **Responsive Design**: Built with Django templates for a responsive user experience

## Technology Stack

- **Backend**: Django 4.1.7
- **Database**: SQLite (default)
- **Authentication**: Django's built-in auth system
- **News API**: NewsAPI for fetching latest news articles
- **Frontend**: Django Templates

## Project Structure

```
Blogs and News site/
├── reg_login/                 # Main Django project
│   ├── manage.py             # Django management script
│   ├── db.sqlite3            # SQLite database
│   ├── requirements.txt       # Python dependencies
│   ├── Procfile               # Deployment configuration
│   ├── media/                 # User uploaded files (images)
│   ├── static/                # Static files (CSS, JS, images)
│   ├── reg_login/             # Main project settings
│   │   ├── settings.py        # Django settings
│   │   ├── urls.py            # URL routing
│   │   ├── asgi.py            # ASGI configuration
│   │   └── wsgi.py            # WSGI configuration
│   ├── main/                  # Main app (home, news)
│   │   ├── views.py           # View functions
│   │   ├── urls.py            # URL patterns
│   │   ├── models.py          # Database models
│   │   └── templates/         # HTML templates
│   └── blogs/                 # Blogs app
│       ├── views.py           # Blog views and logic
│       ├── urls.py            # Blog URL patterns
│       ├── models.py          # Blog models (BlogPost, Comment, Query)
│       ├── forms.py           # Form definitions
│       └── templates/         # Blog templates
└── myenv/                     # Python virtual environment
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (venv)

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anirudhraonh/Blogs-and-News-Site.git
   cd "Blogs and News site"
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows
   python -m venv myenv
   myenv\Scripts\activate

   # macOS/Linux
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   cd reg_login
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`

## Usage

### Home Page
- Visit the home page to see the latest news and application overview

### Create Blog
- Navigate to the "Create Blog" section (login required)
- Fill in the blog title, summary, and optionally add a featured image
- Publish your blog post

### View Blogs
- Browse all published blog posts in the "Blogs" section
- Click on any blog post to view full details
- Read and write comments on blog posts

### Search Blogs
- Use the search form to find blog posts by title
- Results will display matching blog posts

### Admin Panel
- Access the admin panel at `/admin/` with superuser credentials
- Manage users, blog posts, and comments

## Key Models

### BlogPost
- **title**: Blog post title (unique, max 250 characters)
- **summary**: Blog post content/summary
- **posted_at**: Timestamp of post creation
- **posted_by**: Reference to the User who created the post
- **image_small**: Optional featured image

### CommentModel
- **comment**: Comment text (max 150 characters)
- **image**: Optional image attachment
- **comment_by**: Reference to the User who made the comment
- **comment_on**: Reference to the BlogPost being commented on
- **comment_at**: Timestamp of comment creation

### Query
- **query**: Search query text

## Environment Configuration

The application uses the following key settings:

- **DEBUG**: Currently set to `True` (change to `False` in production)
- **ALLOWED_HOSTS**: Set to `["*"]` for development
- **SECRET_KEY**: Defined in `settings.py` (change in production)

## API Integration

The application integrates with **NewsAPI** to fetch and display latest news from multiple sources including:
- BBC News, CNN, Reuters, The Guardian, Bloomberg, TechCrunch, and many more
- Fetches news articles from the past 30 days
- Displays news by relevancy

## Media Management

- User-uploaded images are stored in the `media/images/` directory
- Images are automatically cleaned up from disk when blog posts are deleted
- Supports image uploads for blog posts and comments

## Deployment

The project includes a `Procfile` for deployment on platforms like Heroku. Ensure to:
- Update `DEBUG = False` in production
- Set a secure `SECRET_KEY`
- Configure `ALLOWED_HOSTS` with your domain
- Use a production database (PostgreSQL recommended)
- Use environment variables for sensitive data

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Contact

For questions or suggestions, please reach out to the project maintainer.

## Future Enhancements

- Add email notifications for new comments
- Implement blog post categories/tags
- Add user follow system
- Implement blog post likes/ratings
- Add rich text editor for blog content
- Implement pagination for better performance
- Add API endpoints for mobile app integration

---

**Repository**: [Blogs and News Site](https://github.com/anirudhraonh/Blogs-and-News-Site)
