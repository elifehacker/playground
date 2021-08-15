from pathlib import Path
import files as files
import hashlib

class ImageCacheException(Exception):
    def __init__(self, message: str):
        self.message = message


class ImageCache:
    """
    Caches images on the filesystem.

    It should abide to the following contract:
       * If an image doesn't exist in the cache, it will be downloaded and
         added when first leased (through ImageCache.lease).
       * Downloading an image or returning one from the cache should be
         transparent to the caller. i.e. Leasing an image (through
         ImageCache.lease) will return a Path reference to an image,
         regardless of its presence in the cache before the call to
         ImageCache.lease.
       * An image will exist in the cache until all leases have been released
         (through ImageCache.release)
    """
    def __init__(self, image_client):
        self.lease_counter = dict()
        self.id_counter = 0
        self.image_client = image_client

    def get_path_from_url(self, url) -> Path:
        
        return Path(__file__).parent.resolve()/hashlib.md5(url.encode('utf-8')).hexdigest()

    def lease(self, url: str) -> Path:
        """
        Downloads an image represented by a url or returns a previously
        downloaded image. Regardless, until a leased image is released, the
        file should exist on the file system for other processes to access.

        Args:
            url: The url of the image to download.

        Returns:
            A reference to the location on disk which this image can be accessed at.

        Raises:
            ImageCacheException: An error occurred when leasing
        """
        try:
            image_path = self.get_path_from_url(url)
            if not files.exists(image_path):
                self.lease_counter[image_path] = 0
                files.write(image_path, self.image_client(url))

            self.lease_counter[image_path]+=1
        except Exception as e:
            raise ImageCacheException('')

        return image_path

    def release(self, url: str):
        """
        Releases an image from the cache. After an image is released by all
        processes leasing it, then it is no longer safe for another process to
        access the referenced image file because it will have been deleted.

        Args:
            url: the original url of the image that was leased.

        Raises:
            ImageCacheException: An error occurred when releasing
        """
        try:
            image_path = self.get_path_from_url(url)

            self.lease_counter[image_path]-=1
            if self.lease_counter[image_path] == 0:
                files.delete(image_path)
        except Exception as e:
            raise ImageCacheException('')

