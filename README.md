# 🌐 CoditByNeha — Minimal Front Pag

A clean, fast, and responsive landing page for **CoditByNeha**, a study materials hub covering programming languages, frameworks, backend, and graphics concepts.

---

## 🚀 Overview

This project is a **single-file HTML/CSS/JS** front page with minimal dependencies and fast loading.  
It serves as the **gateway** to the rest of the CoditByNeha site (e.g., `materials.html`, `roadmaps.html`).

### ✨ Features

- **Modern UI** — built with pure HTML & CSS (no frameworks)
- **Responsive layout** — adapts from desktop to mobile
- **Minimal distractions** — only key sections shown
- **Keyboard shortcut:** `/` focuses the search bar
- **Light/Dark mode auto-detection** — respects system preferences
- **Accessible navigation** and semantic structure

---

## 🧱 Structure

### Links
The buttons and quick links route to:
- `materials.html` – main study materials grid  
- `roadmaps.html` – learning paths and plans  

You can rename or change these destinations as needed.

---

## 🖌️ Customization

1. **Branding**
   - Update the text inside `<title>` and `.brand`.
   - Change the logo background colors inside the CSS variable `--primary` and `--accent`.

2. **Navigation**
   - Modify header links or add new pages.

3. **Quick Links**
   - Edit the four `.card` elements in the “Quick Links” section to match your categories.

4. **Search**
   - The search form uses a `GET` action to `materials.html`.  
     You can integrate a real search engine or JavaScript filtering later.

---

## ⚙️ Setup & Deployment

No build step required — just open `index.html` in your browser.

### To deploy:
- **Vercel / Netlify / GitHub Pages:** Drag and drop this file (or the full site folder).
- **Manual Hosting:** Place `index.html` in your server root directory.

---

## 💡 Shortcuts

| Key | Action |
|-----|--------|
| `/` | Focus search bar |
| —   | Auto light/dark theme detection |

---

## 🧠 Credits

- Designed and coded by **Neha Rajput**  
- Part of the **CoditByNeha** study ecosystem  
- Font: [Inter](https://fonts.google.com/specimen/Inter)

---

## 📄 License

Open-source project under the **MIT License**.  
Feel free to modify, share, or extend this design.


