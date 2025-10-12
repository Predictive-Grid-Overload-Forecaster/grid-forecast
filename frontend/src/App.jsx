import React from "react";
import { BrowserRouter } from "react-router";
import AppRoutes from "./assets/Components/Routing/Routing";
import Navbar from "./assets/pages/Navbar";
import DataProvider from "./assets/Components/context/ContextProvider.jsx";

const App = () => {
    return (
        <BrowserRouter>
            <DataProvider>
                <Navbar />
                <AppRoutes />
            </DataProvider>
        </BrowserRouter>
    );
};

export default App;
