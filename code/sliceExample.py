@DEVICE.route("/")
def get_all_devices_by_brand() -> Response:
    try:
        page_number = args.get("page_number")
        page_size = args.get("page_size")
        sort_mode = args.get("sort_mode", "ascending")
        devices = get_device_list_by_brands(db)
        sorted_devices = sort_devices(devices, sort_mode)
        result = {
            "data": sorted_devices,
            "total": len(devices),
            "totalPhones": count_phones(devices),
        }
        if page_size and page_number and sort_mode:
            start_index: int = (int(page_number) - 1) * int(page_size)
            end_index: int = start_index + int(page_size)
            result = {
                "data": sorted_devices[start_index:end_index],
                "total": len(devices),
                "totalPhones": count_phones(devices),
            }
        return jsonify(result)
    except Exception as e:
        return Response(str(e), status=500)
