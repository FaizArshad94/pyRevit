# pylint: skip-file
import hooks_logger as hl
hl.log_hook(__file__,
    {
        "cancellable?": str(__eventargs__.Cancellable),
        "doc_type": str(__eventargs__.DocumentType),
        "doc_path": str(__eventargs__.PathName),
    }
)