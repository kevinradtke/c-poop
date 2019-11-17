import { createStyles, Theme, makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    nested: {
      paddingLeft: theme.spacing(6)
    },
    avatar: {
      backgroundColor: "transparent"
    }
  })
);

export default useStyles;
