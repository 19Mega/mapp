import React, { Component, useContext } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { BackendURL } from "./component/backendURL";

import { Home } from "./pages/home";

//import { Navbar } from "./component/navbar";
//import { Footer } from "./component/footer";

import { Context } from "./store/appContext";



//create your first component
const Layout = () => {
    //the basename is used when your project is published in a subdirectory and not in the root of the domain
    // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
    const basename = process.env.BASENAME || "";
    const { store, actions } = useContext(Context);

    if(!process.env.BACKEND_URL || process.env.BACKEND_URL == "") return <BackendURL/ >;

    return (
        <div>
            <BrowserRouter basename={basename}>
                <ScrollToTop>
                    <Navbar />
                    <Routes>
                        <Route element={<Home />} path="/" />
                        <Route element={<h1>Not found!</h1>} />
                        
                        <Route element={<DocsIntro />} path="docs/getting-started/introduction" />

                    </Routes>
                    <Footer/>
                    {/* {window.location.pathname === "/login" || window.location.pathname === "/signup" ? null : <Footer />} */}
                    {/* {store.auth ? <Footer/> : null } */}
                    </ScrollToTop>
                </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
