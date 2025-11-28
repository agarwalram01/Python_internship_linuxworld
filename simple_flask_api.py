from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return"""
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Ram Portfolio</title>

  <!-- INLINE CSS -->
  <style>
    /* Reset & Base Styles */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: "Poppins", sans-serif;
    }

    body {
      background: #fdfdfd;
      color: #333;
      line-height: 1.6;
    }

    /* Navbar */
    .navbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 60px;
      background: #fff;
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .logo {
      font-size: 24px;
      font-weight: 700;
      color: #1a2c5b;
    }
    .logo span {
      color: orange;
    }

    .nav-links {
      list-style: none;
      display: flex;
      gap: 25px;
    }
    .nav-links a {
      text-decoration: none;
      color: #333;
      font-weight: 500;
      transition: 0.3s;
    }
    .nav-links a:hover {
      color: orange;
    }

    .menu-toggle {
      display: none;
      font-size: 26px;
      cursor: pointer;
    }

    /* Hero Section */
    .hero {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 70px 60px;
      flex-wrap: wrap;
      background: linear-gradient(to right, #fff, #f9f9f9);
    }
    .hero-text {
      flex: 1;
      min-width: 300px;
      margin-right: 20px;
    }
    .hero-text h1 {
      font-size: 36px;
      color: #1a2c5b;
      margin-bottom: 15px;
    }
    .hero-text p {
      color: #555;
      font-size: 16px;
    }
    .highlight {
      color: orange;
      font-weight: 600;
    }
    .hero-buttons {
      margin-top: 20px;
    }
    .btn-primary,
    .btn-secondary {
      text-decoration: none;
      padding: 12px 25px;
      border-radius: 6px;
      font-weight: 600;
      transition: 0.3s;
    }
    .btn-primary {
      background: orange;
      color: #fff;
    }
    .btn-secondary {
      background: #1a2c5b;
      color: #fff;
      margin-left: 10px;
    }
    .btn-primary:hover {
      background: #e69500;
    }
    .btn-secondary:hover {
      background: #16244a;
    }

    .hero-image img {
      width: 280px;
      border-radius: 12px;
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
    }

    /* Expertise */
    .expertise {
      text-align: center;
      padding: 70px 40px;
    }
    .expertise h2 {
      color: #1a2c5b;
      font-size: 28px;
    }
    .sub-text {
      color: orange;
      margin-bottom: 10px;
    }
    .skills {
      margin-top: 25px;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 12px;
    }
    .skills span {
      background: #eee;
      padding: 10px 15px;
      border-radius: 6px;
      transition: 0.3s;
    }
    .skills span:hover {
      background: orange;
      color: #fff;
    }

    /* Portfolio */
    .portfolio {
      text-align: center;
      padding: 70px 40px;
      background: #fff;
    }
    .cards {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 25px;
      margin-top: 30px;
    }
    .card {
      background: linear-gradient(135deg, orange, #1a2c5b);
      color: #fff;
      padding: 25px;
      border-radius: 10px;
      width: 300px;
      transition: transform 0.3s;
    }
    .card:hover {
      transform: translateY(-5px);
    }
    .card h3 {
      margin: 15px 0;
    }

    /* Testimonials */
    .testimonials {
      background: #f7f7f7;
      text-align: center;
      padding: 70px 40px;
    }
    .testimonial-list {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 25px;
      margin-top: 30px;
    }
    .testimonial {
      background: #fff;
      padding: 25px;
      border-radius: 10px;
      width: 300px;
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
    }
    .testimonial p {
      font-style: italic;
    }
    .testimonial h4 {
      color: orange;
      margin-top: 10px;
    }

    /* Contact */
    .contact {
      background: #fff;
      padding: 70px 60px;
    }
    .contact-container {
      display: flex;
      flex-wrap: wrap;
      gap: 40px;
    }
    .contact-info {
      flex: 1;
      min-width: 250px;
    }
    .contact-form {
      flex: 1;
      min-width: 300px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .contact-form input,
    .contact-form textarea {
      padding: 12px;
      border: 1px solid #ccc;
      border-radius: 6px;
    }
    .contact-form button {
      background: orange;
      color: #fff;
      border: none;
      padding: 12px;
      border-radius: 6px;
      font-weight: 600;
      transition: 0.3s;
    }
    .contact-form button:hover {
      background: #e69500;
    }

    /* Footer */
    footer {
      text-align: center;
      padding: 20px;
      background: #1a2c5b;
      color: #fff;
    }

    /* Responsive */
    @media (max-width: 992px) {
      .hero {
        flex-direction: column;
        text-align: center;
      }
      .hero-text {
        margin-right: 0;
      }
      .hero-image img {
        margin-top: 20px;
      }
      .cards, .testimonial-list {
        flex-direction: column;
        align-items: center;
      }
      .contact-container {
        flex-direction: column;
      }
    }

    @media (max-width: 768px) {
      .nav-links {
        display: none;
        flex-direction: column;
        background: #fff;
        position: absolute;
        top: 70px;
        right: 0;
        width: 200px;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
      }
      .nav-links.show {
        display: flex;
      }
      .menu-toggle {
        display: block;
      }
    }
  </style>

  <script>
    // Mobile toggle menu
    document.addEventListener("DOMContentLoaded", function () {
      const menuToggle = document.querySelector(".menu-toggle");
      const navLinks = document.querySelector(".nav-links");

      menuToggle.addEventListener("click", () => {
        navLinks.classList.toggle("show");
      });
    });
  </script>
</head>

<body>

  <!-- =================== NAVBAR =================== -->
  <header>
    <nav class="navbar">
      <div class="logo">Ram<span>Portfolio</span></div>
      <ul class="nav-links">
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Projects</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
      <div class="menu-toggle">☰</div>
    </nav>
  </header>

  <!-- =================== HERO =================== -->
  <section class="hero">
    <div class="hero-text">
      <h1>Frontend Developer & UI/UX Designer</h1>
      <p>
        I create <span class="highlight">responsive, user-centric web applications</span> with modern technologies.
      </p>
      <div class="hero-buttons">
        <a href="#" class="btn-primary">View Portfolio</a>
        <a href="#" class="btn-secondary">Hire Me</a>
      </div>
    </div>

    <div class="hero-image">
      <img src="Snapchat-1151375136.jpg" alt="Ram Photo" />
    </div>
  </section>

  <!-- =================== EXPERTISE =================== -->
  <section class="expertise">
    <h2>Professional Expertise</h2>
    <p class="sub-text">Crafting Digital Excellence</p>

    <div class="skills">
      <span>HTML5 & CSS3</span>
      <span>JavaScript ES6+</span>
      <span>React.js</span>
      <span>Vue.js</span>
      <span>TypeScript</span>
      <span>Responsive Design</span>
      <span>UI/UX Design</span>
      <span>REST APIs</span>
      <span>Git & GitHub</span>
      <span>Agile</span>
    </div>
  </section>

  <!-- =================== PORTFOLIO =================== -->
  <section class="portfolio">
    <h2>Portfolio Highlights</h2>

    <div class="cards">
      <div class="card">
        <div class="icon">📈</div>
        <h3>Financial Analytics Dashboard</h3>
        <p>Investment tracking dashboard with real-time charts.</p>
        <a href="#" class="btn-primary">View</a>
      </div>

      <div class="card">
        <div class="icon">🛍️</div>
        <h3>E-Commerce Platform</h3>
        <p>Online store with filters, cart & smooth checkout.</p>
        <a href="#" class="btn-primary">View</a>
      </div>

      <div class="card">
        <div class="icon">📱</div>
        <h3>Health & Fitness App</h3>
        <p>Workout planner and progress tracking mobile app.</p>
        <a href="#" class="btn-primary">View</a>
      </div>
    </div>
  </section>

  <!-- =================== TESTIMONIALS =================== -->
  <section class="testimonials">
    <h2>Client Testimonials</h2>

    <div class="testimonial-list">
      <div class="testimonial">
        <p>“Ram's clean coding style made our app far better than expected.”</p>
        <h4>Sarah Johnson</h4>
        <span>Product Manager</span>
      </div>

      <div class="testimonial">
        <p>“Professional, skilled & creative — he transformed our idea beautifully.”</p>
        <h4>Michael Brown</h4>
        <span>CTO</span>
      </div>
    </div>
  </section>

  <!-- =================== CONTACT =================== -->
  <section class="contact">
    <h2>Get In Touch</h2>

    <div class="contact-container">
      <div class="contact-info">
        <h3>Let’s Build Something Great</h3>
        <p>Open to freelance work & collaborations.</p>
        <p>📧 contact@ramportfolio.com</p>
        <p>📞 +91 9586998822</p>
        <p>📍 Jaipur, Rajasthan</p>
      </div>

      <form class="contact-form">
        <input type="text" placeholder="Full Name" required />
        <input type="email" placeholder="Business Email" required />
        <input type="text" placeholder="Company" />
        <textarea placeholder="Project Details"></textarea>
        <button type="submit">Send Message</button>
      </form>
    </div>
  </section>

  <footer>
    <p>© 2025 Ram Portfolio | All Rights Reserved</p>
  </footer>

</body>
</html>

    """

if __name__ =='__main__':
     app.run()(debug=True)