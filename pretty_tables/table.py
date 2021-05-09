from matplotlib.artist import Artist


class Table(Artist):
    """
    A table used to represent tabular information


    Attributes
    ----------
    m : int
        The number of cells in a row, if no cells are merged. m 
    n : int
        The number of cells in a column, if no cells are merged. 
    n_cells : int
    """

    def __init__(self, data, ax, infer_row_column_labels = True, n_rows = None, n_columns = None, headers = None, row_labels = None):
        """
        Parameters
        ----------
        data : array_like
            holds all of the table data and assumes row and column labels are included unless `infer_row_column_lablels` is `False`
        ax : `mpl.axes.Axes <https://matplotlib.org/stable/api/axes_api.html>` instance.
        infer_row_column_lablels : bool, default=True
            set to False if the class should NOT assume that the x[0][:] are the headers (column titles) and x[:][0] are the row labels
        n_rows : int, default=None
            the number of rows of the, ignored if x is not None
        n_columns : int, default=None
            the number of columns, ignored if x is not None
        headers : array_like, default=None
            0 < len(headers) <= m, array of values to use as headers, if row_labels is not None and len(row_labels) == n and len(headers) == m and the values at headers[0] != row_labels[0], an error is raised to notify the user of ambiguity for the [0,0] value
        row_labels : array_like, default=None
            0 < len(headers) <= n, array of values to use as row labels, if headers is not None and len(row_labels) == n and len(headers) == m and the values at row_labels[0] != headers[0], an error is raised to notify the user of ambiguity for the [0,0] value
        styler : TableStyler
            The `pretty_tables.table.TableStyler` that will format the cells in the rows and columns
        """
        pass

    def __str__(self):
        """
        """
        pass

    def __repr__(self):
        """
        """
        pass

    def __getitem__(self):
        """
        """
        pass

    def __setitem__(self):
        """
        """
        pass

    def merge_cells(self):
        """
        """
        pass


class Cell():
    """
    """

    def __init__(self):
        """
        """
        pass

    def __str__(self):
        """
        """
        pass

    def __repr__(self):
        """
        """
        pass

class TableStyler():
    """
    A class that styles a table. This class can be used to customize the look of a table,
    but a default format will be inferred from the table data.
    """

    def __init__(self, style, header_color = None, odd_row_color = None, even_row_color = None):
        """
        Parameters
        ----------
        style : string
            one of the styles available from the matplotlib style sheets
        header_color : color
            the color of all of the non-hidden cells in the very top row of the table, ignored if style is not None
        odd_row_color : color
            the color to use for every odd row of x, ignored if style is not None
        even_row_color : color
            the color to use for every even row of x, ignored if style is not None
        """
        pass

    def infer_style(self, data):
        """
        """
        pass