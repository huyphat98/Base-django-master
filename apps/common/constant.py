class Language:
    VI = 'vi'
    EN = 'en'


class Error:
    code = "code"
    message = 'message'


class ErrorCode:
    UNKNOWN_ERROR = {
        Error.code: 1001,
        Error.message: {
            Language.VI: 'Đã có lỗi xảy ra',
            Language.EN: 'An error has occurred',
        }
    }
    INVALID_AUTH = {
        Error.code: 1002,
        Error.message: {
            Language.VI: 'Xác thực không hợp lệ',
            Language.EN: 'Invalid authentication',
        }
    }
    NOT_AUTH = {
        Error.code: 1003,
        Error.message: {
            Language.VI: 'Cần đăng nhập để sử dụng chức năng này',
            Language.EN: 'Need login to using this function',
        }
    }
    NOT_PERMISSION = {
        Error.code: 1004,
        Error.message: {
            Language.VI: 'Bạn không có quyền thực hiện hành động này.',
            Language.EN: 'You do not have permission to perform this action.',
        }
    }
    THROTTLED_REQUEST = {
        Error.code: 1005,
        Error.message: {
            Language.VI: 'Quyền truy cập bị hạn chế, có thể bạn đã đưa ra quá nhiều yêu cầu vào lúc này,',
            Language.EN: 'Access is restricted, you may have made too many requests at the moment',
        }
    }
    NOT_FOUND = {
        Error.code: 1006,
        Error.message: {
            Language.VI: 'Không tìm thấy bản ghi',
            Language.EN: 'Not found record',
        }
    }
    NOT_ALLOW_METHOD = {
        Error.code: 1007,
        Error.message: {
            Language.VI: 'Phương thức này không cho phép',
            Language.EN: 'This method is not allowed.',
        }
    }
    LOGIN_FAIL = {
        Error.code: 1008,
        Error.message: {
            Language.VI: 'Tên đăng nhập hoặc mật khẩu không đúng',
            Language.EN: 'Username or password incorrect',
        }
    }
