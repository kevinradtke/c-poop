import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      backgroundColor: "#2F3129"
    },
    h3: {
      marginTop: theme.spacing(0),
      marginBottom: theme.spacing(0),
      paddingTop: theme.spacing(2),
      marginLeft: theme.spacing(1)
    }
  })
);

export default useStyles;
