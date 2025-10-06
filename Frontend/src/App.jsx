import React from "react";
import { BrowserRouter } from "react-router";

import AppRoutes from "./assets/Components/Routing/Routing";
import Navbar from "./assets/pages/Navbar";

const App = () => {
    

    return (
        <BrowserRouter >
            <Navbar />
            <AppRoutes />
        </BrowserRouter>
    )
}

export default App;