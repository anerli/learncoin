import {Outlet, Link} from "react-router-dom";

const Login = () => {
    return (
        <>
            <nav>
                <ul>
                    <li>
                        <Link to="/homepage">Home</Link>
                    </li>
                    <li>
                        <Link to="/signup">Signup</Link>
                    </li>
                    <li>
                        <Link to="/mining">Mining</Link>
                    </li>
                    <li>
                        <Link to="/blockchain">Blockchain</Link>
                    </li>
                </ul>
            </nav>

            <Outlet />
        </>
    )
};

export default Login;