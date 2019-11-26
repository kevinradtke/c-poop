import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";
import { green } from "@material-ui/core/colors";

console.log(green[500]);

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      flexGrow: 1
    },
    appbar: {
      backgroundColor: theme.palette.primary.main
    },
    title: {
      flexGrow: 1
    },
    translateButton: {
      marginRight: theme.spacing(4)
    },
    reset: {
      marginRight: theme.spacing(4),
      color: green[500],
      "&:hover": {
        backgroundColor: "rgb(76, 175, 80, 0.2)"
      }
    }
  })
);

export default useStyles;
