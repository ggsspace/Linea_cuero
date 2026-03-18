<<<<<<< HEAD
import Card from "../../components/card/Card.jsx";
import productos from "./Products.js"; 
import "./Products.css";

const Products = () => {
  return (
    <main>
      <section className="productos-section">
        <h2 className="productos-titulo">Nuestros Productos</h2>
        <div className="cards-container">
          {productos.map((producto) => (
            <Card key={producto.id} {...producto} />
          ))}
        </div>
      </section>
    </main>
  );
};

export default Products;
=======
import react from "react";
import "./Products.css";

const  Products = () => {
  return (
    <main>
      <h1>Productos</h1>

    </main>
  );
};
export default Products;



>>>>>>> dd166d1ab92abb87eac3c5e9c25288db4980fe45
