from unittest.mock import patch

from workspace.__main__ import main


@patch("builtins.print")
def test_worspace_entrypoint(mock_print):
    main()

    mock_print.assert_called_with("Hello World!")
