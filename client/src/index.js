import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { CookiesProvider } from "react-cookie";

import './index.css';
import Blockchain from './Pages/Blockchain';
import Homepage from "./Pages/Homepage";
import Landing from "./Pages/Landing";
import Layout from "./Pages/Layout";
import Learning from "./Pages/Learning";
import Login from "./Pages/Login";
import Mining from "./Pages/Mining";
import Signup from "./Pages/Signup";

export default function App() {
    return (
        <CookiesProvider>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Layout />}>
                        <Route index element={<Landing />} />
                        <Route path="homepage" element={<Homepage />} />
                        <Route path="signup" element={<Signup />} />
                        <Route path="mining" element={<Mining />} />
                        <Route path="blockchain" element={<Blockchain />} />
                        <Route path="login" element={<Login />} />
                        <Route path="learning" element={<Learning />} />
                        <Route
                            path="*"
                            element={
                                <main>
                                    <h2>This page does not exist!</h2>
                                </main>
                            }
                        />
                    </Route>
                </Routes>
            </BrowserRouter>
        </CookiesProvider>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));
