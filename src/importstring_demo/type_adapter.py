from pydantic import ImportString, TypeAdapter

pandas = TypeAdapter(ImportString).validate_python("pandas")
