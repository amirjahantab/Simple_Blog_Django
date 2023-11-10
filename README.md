# Simple Django Blog

This is a basic Django blog application consisting of views to display a list and details of blog articles.

## Views

### `blog_list` View
- Path: `/blog/list/`
- Description: Displays a list of blog articles.
- Renders the `list.html` template with a list of articles.

### `blog_detail` View
- Path: `/blog/<slug>/`
- Description: Shows the details of a specific blog article.
- Retrieves and renders the `detail.html` template with the content of the specified article.

## Models

### `Article` Model
- Attributes:
  - `title`: Title of the article (max 200 characters).
  - `content`: Content of the article (text field).
  - `created`: Date and time of creation.
  - `edited`: Last edit date and time.
  - `author`: ForeignKey to User model.
  - `status`: Article status (`checking`, `rejected`, `published`).
  - `slug`: Unique slug for the article (based on title and date).
  - `image`: Optional image for the article.
- Custom Method:
  - `save`: Overrides the save method to automatically generate a slug for the article based on the title and date.
- Managers:
  - `objects`: Default manager.
  - `publish`: Custom manager to retrieve only published articles.

### Article Methods
- `__str__()`: String representation of the article.
- `get_absolute_url()`: Method to get the URL of the article.

## Usage
To use this blog application:
1. Define URL patterns in your Django project's `urls.py` file to link to the `blog_list` and `blog_detail` views.
2. Create corresponding HTML templates (`list.html` and `detail.html`) to display the list and details of articles.
3. Integrate the `Article` model in your Django project, and define appropriate URLs and templates.

## Note
Make sure to set up URL mappings, templates, and include the necessary styling and design to render the views properly.

---
