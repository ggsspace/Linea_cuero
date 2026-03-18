import "./Home.css";
import { NavLink } from "react-router-dom";

import Cart from "../../components/cart/Cart.jsx";
import Products from "../products/Products";


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

        <button className="hero-cta-btn">Explorar Productos</button>
      </section>

      

    </main>
    
    
  );
};


export default Home;

