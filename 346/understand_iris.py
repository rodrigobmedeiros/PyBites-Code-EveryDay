__all__ = [
    "IRIS_DATA",
    "get_nr_classes",
    "get_nr_samples",
    "get_dim",
    "get_nr_samples_per_class",
    "get_rel_nr_samples_per_class",
    "get_nr_missing_values",
    "get_stats_per_feature",
    "get_correlation_per_feature",
] # __all__ controls what gets imported if you use from module.py import *.
import pandas as pd
from sklearn.datasets import load_iris

# you can set as_frame to False, but this will complicate the solution
# because you have to work with numpy ndarrays
IRIS_DATA = load_iris(as_frame=True, return_X_y=True)


def get_nr_classes(data: tuple) -> int:
    """Return the number of classes in the Iris data set.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        int: Number of classes (targets) in the data set.
    """

    classes = data[1].unique()
    number_of_classes = len(classes)
    return number_of_classes

def get_nr_samples(data: tuple) -> int:
    """Return the number of samples in the Iris data set.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        int: Number of samples (instances) in the data set.
    """

    samples = data[0]
    number_of_samples = len(samples)
    return number_of_samples

def get_dim(data: tuple) -> int:
    """Return the dimensionality of the Iris data set.

    **Warning**: Dimensionality is not meant in the mathematical sense
        (which would be the shape and dim attribute if we would talk about matrices).
        Dimensionality in ML means the number of dimensions in your data,
        that is the number of axes your data span over, which is the number of features we
        have available.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        int: Number of dimensions (features) in the data set.
    """
    samples = data[0]
    dimension = samples.shape[1]
    return dimension

def get_nr_samples_per_class(data: tuple) -> pd.Series:
    """Return the number of samples for each class of the Iris data set.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        pd.Series: Series with number of samples for each class.
    """

    samples = data[1]
    samples_per_class = samples.value_counts()
    return samples_per_class

def get_rel_nr_samples_per_class(data: tuple) -> pd.Series:
    """Return the relative number of samples for each class of the Iris data set.

    **Hint**: Try to re-use already defined functions.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        pd.Series: Series with percentage (between 0 and 1) of samples for each class.
    """
    return get_nr_samples_per_class(data) / get_nr_samples(data)


def get_nr_missing_values(data: tuple) -> int:
    """Return the number of missing values in the Iris data set.

    **Hint**: pandas isna() might come in handy.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        int: Number of missing values in the data set.
    """
    # sum can only sum along axis 0 (indices) or 1 (columns), so we need to call it twice
    samples = data[0]
    samples_nan = samples.isna()
    total_nan = samples_nan.sum().sum()
    return total_nan


def get_stats_per_feature(
    data: tuple,
    features: list,
    stats: list,
) -> pd.DataFrame:
    """Return summary statistics for a list of given features.

    **Hint**: Maybe try out pandas.DataFrame.describe() or pandas.DataFrame.agg().

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().
        features (list): A list of features for which to calculate summary statistics.
        stats (list): A list of summary statistics to calculate/extract for the given features.

    Returns:
        pd.DataFrame: A data frame with the requested summary statistics for each feature.
    """
    samples = IRIS_DATA[0]
    stats_data = samples.describe()
    stats_df = stats_data.loc[stats, features]
    return stats_df


def get_correlation_per_feature(
    data: tuple,
    features: list,
) -> pd.DataFrame:
    """Return feature correlation with target.

    **Hint**: Correlation coefficients can be calculated for each pair of feature with pandas.DataFrame.corr().
        This means you might have to combine the features and the target into a single data frame.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().
        features (list): A list with feature names for which the correlation is returned.

    Returns:
        pd.Series: Value of feature correlation with target.
    """
    complete_data = IRIS_DATA[0]
    target = IRIS_DATA[1]
    complete_data['target'] = target
    corr_df = complete_data.corr()
    return corr_df.loc[features, 'target']

if __name__ == "__main__":
    # here you can try out your functions!
    # only called when directly run so no problem when imported from the test file
    print(IRIS_DATA[0].head()) # show the first 5 lines.
    print(get_nr_classes(IRIS_DATA)) # pass the data to the function and return nr classes.
    print(get_rel_nr_samples_per_class(IRIS_DATA))