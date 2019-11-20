import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";

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
    }
  })
);

export default useStyles;
