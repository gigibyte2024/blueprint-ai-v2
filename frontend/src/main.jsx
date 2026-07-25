import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { Toaster } from "sonner";

import "./index.css";
import AppRouter from "./router/AppRouter";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <AppRouter />

      <Toaster
        position="top-right"
        richColors
        theme="dark"
        closeButton
        duration={3000}
      />
    </BrowserRouter>
  </React.StrictMode>,
);
