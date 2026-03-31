# How It  Works 
The `gallery.html` and `index.html` files work together in Jekyll to display a **lightbox gallery** (`thumbs`) and an **inline carousel** (`carousel`) using the **blueimp Gallery** library. 


🌐 GitHub - blueimp/Gallery: blueimp Gallery is a touch-enabled, ...
https://github.com/blueimp/Gallery


## How These Files Work Together

### 1. **Data Definition (`index.html`)**
The front matter in `index.html` defines two arrays:
- `thumbs`: Full list of images for the lightbox gallery.
- `carousel`: Subset of images to display in the inline carousel. 

These are Jekyll data variables accessible within the included `gallery.html`.

### 2. **Template Rendering (`gallery.html`)**
The template uses Liquid to:
- Generate `<a>` tags for the **carousel** (hidden via CSS) from `page.carousel`. 
- Generate `<a>` tags for the **lightbox thumbnails** from `page.thumbs`.
- Both sets of links use `data-gallery` to enable blueimp Gallery functionality. 

### 3. **JavaScript & CSS (Implied)**
Although not shown, external blueimp Gallery JavaScript and CSS must be included. The library uses:
- `data-gallery` attribute to automatically initialize the lightbox on thumbnail clicks.
- The hidden `#carousel-links` content is used to populate the visible `#blueimp-gallery-carousel` div as an inline carousel via JavaScript initialization. 

## Rules for Working Order and Organization

### Image Files
- Store full-size images in `/assets/images/`.
- Store thumbnails in `/assets/images/thumb/`.
- Use consistent naming: `filename.jpg` and `thumb/filename.jpg`.

### Jekyll Front Matter (`index.html`)
- List image **base names** (without extension or path) under `thumbs` and `carousel`.
- Order matters: Images appear in the sequence listed.
- Use `carousel` for featured images to display in the inline carousel.
- Use `thumbs` for all images to appear in the lightbox. 

### HTML Template (`gallery.html`)
- The `#carousel-links` div is hidden (`style="display: none"`) and serves only as a data source.
- The `#links` div displays clickable thumbnails.
- Both use `data-gallery` to trigger the gallery.
- The `#blueimp-gallery-carousel` div is the visible carousel container rendered by JavaScript. 

### Working Flow
1. **Add images** to `/assets/images/` and `/assets/images/thumb/`.
2. **Update `index.html`** front matter: add base filenames to `thumbs` and optionally to `carousel`.
3. **Ensure blueimp Gallery assets** (JS/CSS) are loaded on the page. 
4. **Build and serve** with Jekyll — the gallery and carousel render automatically.


