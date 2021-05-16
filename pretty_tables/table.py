from matplotlib.artist import Artist


class Table(Artist):
    """
    A table used to represent tabular information.


    Attributes
    ----------
    m : int
        The number of cells in a row, if no cells are merged. m 
    n : int
        The number of cells in a column, if no cells are merged. 
    n_cells : int
        The whole number of cells presently in the table. If cells are merged, 
        this will be less than m x n, otherwise it is m x n.
    """

    def __init__(self, data, ax, infer_row_column_labels = True, n_rows = None, n_columns = None, headers = None, row_labels = None):
        """
        Parameters
        ----------
        data : array_like
            holds all of the table data and assumes row and column labels are included unless `infer_row_column_lablels` is `False`
        ax : matplotlib Axes (https://matplotlib.org/stable/api/axes_api.html) instance
            The axis which the table will be drawn to
        infer_row_column_lablels : bool, default=True
            set to `False` if the class should NOT assume that the `data[0][:]` are the headers (column titles) and `data[:][0]` 
            are the row labels
        n_rows : int, default=None
            the number of rows of the, ignored if `data` is not `None`
        n_columns : int, default=None
            the number of columns, ignored if `data` is not `None`
        headers : array_like, default=None
            `0 < len(headers) <= m`, array of values to use as headers, if `row_labels` is not `None` and `len(row_labels) == n` 
            and `len(headers) == m` and the values at `headers[0] != row_labels[0]`, an error is raised to notify 
            the user of ambiguity for the `[0,0]` value
        row_labels : array_like, default=None
            `0 < len(headers) <= n`, array of values to use as row labels, if `headers` is not `None` and `len(row_labels) == n`
            and `len(headers) == m` and the values at `row_labels[0] != headers[0]`, an error is raised to notify 
            the user of ambiguity for the `[0,0]` value
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

    def merge_cells(self, xy_start, xy_grow):
        """
        Merge cells together. Data of the cells that will be grown into will be lost.

        Parameters
        ----------
        xy_start : tuple
            two numbers, `0 < x < m-2` and `0 < y < n-2`, which represent which cell will be expanded by the dimensions in `xy_grow`
        xy_grow : tuple
            two numbers, `1 < x < (m - xy_start[0])` and `1 < y < (n - xy_start[1])` representing
            how far to expand the cell in the `x` and `y` direction of the table
        """
        pass


class Cell():
    """
    A matplotlib Text, a collection of 4 Line2Ds, and a matplotlib Rectangle. The 4 edges are defined
    using Line2Ds so that fine grain control of all edges in possible. The rectangle allows the background
    color to be controlled and spans the full width and height of the cell.

    Attributes
    ----------
    v_pad : int
        The number of points to pad the top and bottom of the Text object. `v_pad / 2` will be above and below
        the text
    h_pad : int
        The number of points to pad the left and right of the Text object. `h_pad / 2` will be above and below
        the text
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

    Notes
    ----------
    The rules below are a direct quote from [1]_.

    1. Do not use vertical lines.
    1. Do not use horizontal lines between data rows. (Horizontal lines as separator between the title row and the first data row or as frame for the entire table are fine.)
    1. Text columns should be left aligned.
    1. Number columns should be right aligned and should use the same number of decimal digits throughout.
    1. Columns containing single characters are centered.
    1. The header fields are aligned with their data, i.e., the heading for a text column will be left aligned and the heading for a number column will be right aligned.


    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
    expert systems and adaptive co-kriging for environmental habitat
    modelling of the Highland Haggis using object-oriented, fuzzy-logic
    and neural-network techniques," Computers & Geosciences, vol. 22,
    pp. 585-588, 1996.
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