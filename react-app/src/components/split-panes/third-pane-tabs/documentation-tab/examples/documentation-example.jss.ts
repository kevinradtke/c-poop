import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    div: {
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center"
    },
    h4: {
      marginLeft: theme.spacing(1)
    },
    codeIcon: {
      marginRight: theme.spacing(3)
    }
  })
);

export default useStyles;
