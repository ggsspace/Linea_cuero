import "./Home.css";
import { NavLink } from "react-router-dom";
<<<<<<< HEAD
=======

import Products from "../products/Products.jsx";

>>>>>>> dd166d1ab92abb87eac3c5e9c25288db4980fe45

const Home = () => {
  return (
    <main>
      <section className="hero-content">
        <h1 className="hero-title">
          Innovación que se viste: El <span className="hero-highlight">talento</span> del CDMC en <span className="hero-highlight">tus manos</span>
        </h1>
        <p className="hero-description">
          Explora una colección exclusiva nacida en el corazón del Centro de Diseño 
          y Manufactura del Cuero. Desde calzado de alta resistencia hasta 
          marroquinería de autor y prendas con sello de innovación. Cada pieza es 
          el resultado de la excelencia técnica y la pasión de nuestros aprendices.
        </p>
<<<<<<< HEAD
        <NavLink to="/productos">
          <button className="hero-cta-btn">Explorar Productos</button>
        </NavLink>
      </section>
=======

        
        <NavLink to = "/products">
        <button className="hero-cta-btn">Explorar Productos</button>
        </NavLink>
      </section>

      

>>>>>>> dd166d1ab92abb87eac3c5e9c25288db4980fe45
    </main>
    
    
  );
};


export default Home;