import React, {Component} from 'react';
import { styled } from '@material-ui/styles';
import Button from '@material-ui/core/Button';
import { Link } from 'react-router-dom';
import './login.css';
import { makeStyles } from '@material-ui/core/styles';
import MenuItem from '@material-ui/core/MenuItem';
import TextField from '@material-ui/core/TextField';

document.body.style = 'background: #9CECFB;';

const MyButton = styled(Button)({
  background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
  border: 0,
  borderRadius: 200,
  boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
  color: 'white',
  height: 48,
  padding: '0 30px',
});

const useStyles = makeStyles(theme => ({
    container: {
      display: 'flex',
      flexWrap: 'wrap',
    },
    textField: {
      marginLeft: theme.spacing(1),
      marginRight: theme.spacing(1),
    },
    dense: {
      marginTop: theme.spacing(2),
    },
    menu: {
      width: 200,
    },
}));

class login extends Component {
    render() {
        return(
            <div style={{width: '100%', margin: 'auto'}} className="form">
                <p> 
                </p>

                <TextField
                    id="name"
                    label="Name"
                    margin="normal"
                    variant="filled"
                />
                <TextField
                    id="password"
                    type="password"
                    label="Password"
                    margin="normal"
                    variant="filled"

                />
                <p>

                </p>
                <Link to="/stream">
                    <MyButton className ="Login">
                        Login
                    </MyButton>
                </Link>

            </div>
        )
    }
}

export default login;