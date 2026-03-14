
const productos = [
  {
    id: 1,
    titulo: "Producto 1",
    descripcion: "Descripción del producto",
    precio: "$10.000",
    imagen: "https://via.placeholder.com/300"
  },
  {
    id: 2,
    titulo: "Producto 2",
    descripcion: "Descripción del producto",
    precio: "$20.000",
    imagen: "https://via.placeholder.com/300"
  },
  {
    id: 3,
    titulo: "Producto 3",
    descripcion: "Descripción del producto",
    precio: "$30.000",
    imagen: "https://via.placeholder.com/300"
  }
];

import React from "react";
import "./Products.css";

const Products = () => {
  return (
    <main>
      <h1>Productos</h1>
    </main>
  );
};


export default productos; 