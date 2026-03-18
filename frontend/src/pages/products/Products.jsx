import Card from "../../components/card/Card.jsx";
import "../products/Products.css";
import { productosData } from "./productsData.js";

const Products = () => {
  return (
    <main>
      <section className="products-section">
        <h2 className="products-title">Nuestros Productos</h2>
        <div className="cards-container">
          {productosData.map((product) => (
            <Card key={product.id} {...product} />
          ))}
        </div>
      </section>
    </main>
  );
};

export default Products;
